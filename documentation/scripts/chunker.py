import re
import json
import yaml
from pathlib import Path
from typing import List, Dict, Tuple
from transformers import AutoTokenizer

# =========================
# Config
# =========================

INPUT_DIR = Path("./documentation/preprocessed")
OUTPUT_FILE = Path("./documentation/dataset/chunks.json")

MAX_TOKENS = 768  # safe margin under model limit (512)

# =========================
# Tokenizer
# =========================

tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-base-en-v1.5")

def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text, add_special_tokens=False))

# =========================
# Regex
# =========================

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")
CODE_FENCE_RE = re.compile(r"```(\w+)?\n([\s\S]*?)```", re.MULTILINE)

# =========================
# Frontmatter
# =========================

def extract_frontmatter(md: str) -> Tuple[Dict, str]:
    match = FRONTMATTER_RE.match(md)
    if not match:
        return {}, md

    fm_text = match.group(1)
    rest = md[match.end():]

    try:
        data = yaml.safe_load(fm_text) or {}
    except Exception:
        data = {}

    return data, rest.lstrip()

# =========================
# Code extraction (per chunk)
# =========================

def extract_codes(text: str) -> Tuple[str, List[Dict]]:
    codes = []
    counter = 1

    def replacer(match):
        nonlocal counter
        lang = match.group(1) or "text"
        code = match.group(2).strip()

        placeholder = f"```{lang}_code_{counter}```"
        codes.append({
            "id": counter,
            "language": lang,
            "code": code
        })
        counter += 1
        return placeholder

    cleaned_text = CODE_FENCE_RE.sub(replacer, text)
    return cleaned_text.strip(), codes

# =========================
# Section splitting
# =========================

def split_sections(md: str) -> List[Dict]:
    sections = []
    lines = md.splitlines()

    in_code = False
    buffer = []
    heading_stack = []

    def flush():
        if buffer:
            sections.append({
                "title": " — ".join(h[1] for h in heading_stack) or "Introduction",
                "content": "\n".join(buffer).strip()
            })

    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            buffer.append(line)
            continue

        if not in_code:
            m = HEADING_RE.match(line)
            if m:
                flush()
                buffer.clear()

                level = len(m.group(1))
                title = m.group(2).strip()

                while heading_stack and heading_stack[-1][0] >= level:
                    heading_stack.pop()

                heading_stack.append((level, title))
                continue

        buffer.append(line)

    flush()
    return sections

# =========================
# Token-safe splitting
# =========================

def split_by_tokens(title: str, text: str) -> List[str]:
    chunks = []
    buffer = []
    tokens = 0

    for line in text.splitlines():
        line_tokens = count_tokens(line + "\n")

        if tokens + line_tokens > MAX_TOKENS:
            chunks.append("\n".join(buffer).strip())
            buffer = []
            tokens = 0

        buffer.append(line)
        tokens += line_tokens

    if buffer:
        chunks.append("\n".join(buffer).strip())

    return [f"{title}\n\n{c}" for c in chunks if c.strip()]

# =========================
# Copy headless language snippets to description file.
# =========================

def move_snippet_to_description(source_file: Path, target_file: Path):
    """
    Appends the content of source_file to target_file.
    
    :param source_file: Path to the markdown file to copy from.
    :param target_file: Path to the markdown file to append to.
    """
    if not source_file.exists():
        raise FileNotFoundError(f"Source file does not exist: {source_file}")

    # Read the source file content
    content_to_add = source_file.read_text(encoding="utf-8")

    # Append to target file
    with target_file.open("a", encoding="utf-8") as f:
        f.write("\n\n")  # optional: add spacing between existing and new content
        f.write(content_to_add)
    source_file.unlink()

def is_code_snippet(path: Path, root: Path) -> bool:
    """
    Returns True if 'path' is inside any folder named 'headless'
    under the given root directory and the file name is not '_description.md'.
    """
    try:
        relative_parts = path.relative_to(root).parts
    except ValueError:
        return False
    return "headless" in relative_parts and path.name.lower() != "_description.md"
# =========================
# Build chunks
# =========================

def build_chunks(md: str, source: Path) -> List[Dict]:
    chunks = []

    frontmatter, body = extract_frontmatter(md)
    sections = split_sections(body)

    order = 0

    for sec_idx, section in enumerate(sections):
        # 1️⃣ Extract code FIRST from content
        clean_content, codes = extract_codes(section["content"])

        # 2️⃣ Combine title + content for embedding
        full_text = f"{section['title']}\n\n{clean_content}".strip()
        total_tokens = count_tokens(full_text)

        # 3️⃣ Decide chunking strategy
        if total_tokens <= MAX_TOKENS:
            parts = [full_text]
        else:
            parts = split_by_tokens(section["title"], clean_content)

        # 4️⃣ Emit chunks
        for part_idx, part in enumerate(parts):
            part_tokens = count_tokens(part)


            chunks.append({
                "chunk_id": f"{source}::{sec_idx}::{part_idx}",
                "order": order,
                "text": part,
                "tokens": part_tokens,
                "source": str(source),
                "section": section["title"],
                "frontmatter": frontmatter,
                "codes": codes
            })
            order += 1

    return chunks

# =========================
# Clean headless files
# =========================
def clean_headless_files(root: Path):
    for md_file in root.rglob("*.md"):
        if is_code_snippet(md_file, root):
            move_snippet_to_description(md_file, md_file.parent / "_description.md")

# =========================
# Directory
# =========================

def chunk_directory(root: Path) -> List[Dict]:
    all_chunks = []
    clean_headless_files(root)
    for md_file in root.rglob("*.md"):
        if md_file.name.lower() == "changelog.md":
            continue

        text = md_file.read_text(encoding="utf-8", errors="ignore")
        all_chunks.extend(build_chunks(text, md_file))

    return all_chunks

# =========================
# Runner
# =========================

if __name__ == "__main__":
    print("🔹 Chunking markdown files...")

    chunks = chunk_directory(INPUT_DIR)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"✅ Generated {len(chunks)} chunks")
    print(f"📄 Saved to {OUTPUT_FILE}")
