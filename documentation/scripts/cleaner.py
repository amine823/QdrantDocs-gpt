import re
import yaml
from pathlib import Path
from typing import Tuple, Dict


# -------------------------
# File IO
# -------------------------
def copy_md_as_is(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

def load_md_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def save_clean_md(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


# -------------------------
# Frontmatter
# -------------------------

FRONTMATTER_PATTERN = re.compile(
    r"^---\s*\n(.*?)\n---\s*\n",
    re.DOTALL
)


def extract_frontmatter(md_text: str) -> Tuple[Dict, str]:
    """
    Returns (frontmatter_dict, body_text)
    """
    match = FRONTMATTER_PATTERN.match(md_text)
    if not match:
        return {}, md_text

    raw_yaml = match.group(1)
    body = md_text[match.end():]

    try:
        frontmatter = yaml.safe_load(raw_yaml) or {}
    except yaml.YAMLError:
        frontmatter = {}

    return frontmatter, body

def filter_frontmatter(frontmatter: Dict) -> Dict:
    """Keep only specified frontmatter fields"""
    keep_fields = {
        "title", "subtitle", "description", "tags", 
        "authors", "url", "source_url", "content"
    }
    filtered = {k: v for k, v in frontmatter.items() if k in keep_fields}
    return filtered
def rebuild_frontmatter(frontmatter: Dict) -> str:
    """Rebuild filtered frontmatter as YAML"""
    if not frontmatter:
        return ""
    
    import yaml
    yaml_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    return f"---\n{yaml_str}---\n"

# -------------------------
# Images
# -------------------------

IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\([^)]+\)")

def remove_images(md_text: str) -> str:
    return IMAGE_PATTERN.sub("", md_text)


# -------------------------
# Code Blocks
# -------------------------

CODE_BLOCK_PATTERN = re.compile(
    r"```(\w+)?\n(.*?)```",
    re.DOTALL
)


def normalize_code_blocks(md_text: str) -> str:
    """
    Ensures code blocks are preserved and normalized.
    No formatting or indentation changes.
    """

    def _normalize(match):
        lang = match.group(1) or ""
        code = match.group(2).rstrip()
        return f"\n```{lang}\n{code}\n```\n"

    return CODE_BLOCK_PATTERN.sub(_normalize, md_text)

def remove_markdown_emphasis(text: str) -> str:
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    return text

BULLET_DASH_PATTERN = re.compile(r"(?<=\s)-(?=\s)")

def remove_bullet_dashes(md_text: str) -> str:
    """
    Remove dash bullets surrounded by whitespace,
    preserve hyphenated words like 'gpt-4o'
    """
    return BULLET_DASH_PATTERN.sub("", md_text)

# -------------------------
# Tables
# -------------------------

TABLE_ROW_PATTERN = re.compile(r"^\|.*\|$")

def is_divider_row(cells: list[str]) -> bool:
    """
    Detect markdown divider rows like:
    |----|----|
    | --- | :--- |
    """
    return all(re.fullmatch(r"[-: ]+", cell) for cell in cells)


def simplify_tables(md_text: str) -> str:
    """
    Convert markdown tables into clean, natural-language text
    optimized for embeddings.
    """

    lines = md_text.splitlines()
    output = []

    table_rows = []
    in_table = False

    def flush_table(rows: list[list[str]]) -> list[str]:
        if len(rows) < 2:
            return []

        headers = [h.strip("* ").lower() for h in rows[0]]
        data_rows = rows[1:]

        rendered = []

        for row in data_rows:
            if len(row) != len(headers):
                continue

            cells = [c.strip() for c in row]
            if not any(cells):
                continue

            # Special case: Step / Description tables
            if "step" in headers and "description" in headers:
                step = cells[headers.index("step")]
                desc = cells[headers.index("description")]

                if step and desc:
                    rendered.append(f"{step}. {desc}")
                elif desc:
                    rendered.append(desc)
                continue

            # Generic table → sentence-like row
            parts = [v for v in cells if v]
            if parts:
                rendered.append(" — ".join(parts))

        return rendered

    for line in lines:
        if TABLE_ROW_PATTERN.match(line):
            in_table = True
            cells = [c.strip() for c in line.strip("|").split("|")]

            # Skip divider rows entirely
            if is_divider_row(cells):
                continue

            table_rows.append(cells)

        else:
            if in_table:
                output.extend(flush_table(table_rows))
                table_rows = []
                in_table = False

            output.append(line)

    # Flush at EOF
    if in_table:
        output.extend(flush_table(table_rows))

    return "\n".join(output)



# -------------------------
# Whitespace
# -------------------------
'''
def normalize_punctuation_spacing(text: str) -> str:
    # Fix spaces before punctuation
    text = re.sub(r"\s+([.,:;!?])", r"\1", text)
    # Fix broken dot spacing inside words (gpt.4o)
    text = re.sub(r"(\w)\.\s+(\w)", r"\1.\2", text)
    return text
'''
def normalize_inline_spacing(md_text: str) -> str:
    """
    Collapse multiple spaces into one,
    but ONLY outside fenced code blocks.
    """

    result = []
    in_code_block = False
    i = 0
    n = len(md_text)

    while i < n:
        # Toggle code block
        if md_text[i:i+3] == "```":
            in_code_block = not in_code_block
            result.append("```")
            i += 3
            continue

        if not in_code_block:
            # Collapse runs of spaces
            if md_text[i] == " ":
                result.append(" ")
                while i < n and md_text[i] == " ":
                    i += 1
                continue

        result.append(md_text[i])
        i += 1

    return "".join(result)

def normalize_whitespace(md_text: str) -> str:
    # Remove trailing spaces
    md_text = re.sub(r"[ \t]+$", "", md_text, flags=re.MULTILINE)

    # Normalize line endings
    md_text = md_text.replace("\r\n", "\n")

    # Collapse excessive blank lines (max 2)
    md_text = re.sub(r"\n{3,}", "\n\n", md_text)

    return md_text.strip()


# -------------------------
# Layout-only Detection
# -------------------------

def is_layout_only(frontmatter: Dict, body: str) -> bool:
    """
    Detects UI/config-only markdown files.
    """
    if not body.strip():
        return True

    has_header = bool(re.search(r"^#{1,3}\s+", body, re.MULTILINE))
    return not has_header

# -------------------------
# HTML Tags AND LINKS(Outside Code)
# -------------------------

def remove_html_tags_and_links_outside_code(md_text: str) -> str:
    """
    Remove HTML tags and collapse Markdown links [text](url) → text
    outside code blocks. Preserve code blocks verbatim.
    """

    result = []
    in_code_block = False
    i = 0
    n = len(md_text)

    while i < n:
        # Toggle code block state
        if md_text[i:i+3] == '```':
            in_code_block = not in_code_block
            result.append('```')
            i += 3
            continue

        if not in_code_block:
            # 1. Remove HTML tags
            if md_text[i] == '<':
                tag_end = md_text.find('>', i)
                if tag_end != -1:
                    i = tag_end + 1
                    continue

            # 2. Collapse Markdown links [text](url) → text
            if md_text[i] == '[':
                close_bracket = md_text.find(']', i + 1)
                if close_bracket != -1 and close_bracket + 1 < n and md_text[close_bracket + 1] == '(':
                    close_paren = md_text.find(')', close_bracket + 2)
                    if close_paren != -1:
                        link_text = md_text[i + 1:close_bracket]
                        result.append(link_text)
                        i = close_paren + 1
                        continue

            # 3. Skip bare URLs entirely
            if md_text[i:i+7] == 'http://' or md_text[i:i+8] == 'https://' or md_text[i:i+4] == 'www.':
                i += 1
                while i < n and md_text[i] not in ' \n\t':
                    i += 1
                continue

            result.append(md_text[i])

        else:
            result.append(md_text[i])

        i += 1

    return ''.join(result)

def remove_remaining_html(md_text: str) -> str:
    return re.sub(r"<[^>]+>", "", md_text)

def replace_remaining_urls_with_semantics(text: str) -> str:
    # Qdrant support
    text = re.sub(
        r'https?://support\.qdrant\.io/?',
        'the Qdrant support portal',
        text
    )

    # Qdrant dashboard
    text = re.sub(
        r'https?://localhost:6333/?',
        'the local Qdrant dashboard',
        text
    )

    # Local API docs (any port)
    text = re.sub(
        r'https?://localhost:\d+/docs/?',
        'the local API documentation interface',
        text
    )

    # Any remaining URLs
    text = re.sub(
        r'https?://\S+',
        'the linked resource',
        text
    )

    return text

# -------------------------
# Filler Lines
# -------------------------

FILLER_LINE_PATTERN = re.compile(r'^[-=*_#]{3,}$', re.MULTILINE)

def remove_filler_lines(md_text: str) -> str:
    """Remove lines filled only with repeated -, =, *, _, # (3+ chars)"""
    return FILLER_LINE_PATTERN.sub('', md_text)

def remove_empty_lines(md_text: str) -> str:
    """
    Removes all empty lines (including whitespace-only lines) from Markdown.
    Preserves Markdown structure (headers, code blocks, lists).
    """
    lines = md_text.splitlines()
    clean_lines = [line for line in lines if line.strip()]  # Keep non-empty lines
    return '\n'.join(clean_lines)
# -------------------------
# Orchestrator
# -------------------------

def clean_markdown(md_text: str) -> str:
    md_text = remove_images(md_text)
    md_text = remove_html_tags_and_links_outside_code(md_text)
    md_text = remove_filler_lines(md_text)
    md_text = normalize_code_blocks(md_text)
    md_text = simplify_tables(md_text)
    md_text = remove_remaining_html(md_text)
    md_text = replace_remaining_urls_with_semantics(md_text)
    md_text = remove_markdown_emphasis(md_text)
    md_text = remove_bullet_dashes(md_text)
    md_text = normalize_whitespace(md_text)
    md_text = normalize_inline_spacing(md_text)
    md_text = remove_empty_lines(md_text)
    return md_text

# -------------------------
# Directory Processing
# -------------------------
# skips "headless" folders
def is_under_headless(path: Path, root: Path) -> bool:
    """
    Returns True if 'path' is inside any folder named 'headless'
    under the given root directory.
    """
    try:
        relative_parts = path.relative_to(root).parts
    except ValueError:
        return False

    return "headless" in relative_parts

def remove_generated_from_path(path: Path, root: Path) -> Path:
    """
    Given a file path under root, return a relative path
    with any 'generated' directory removed.
    """
    relative_parts = path.relative_to(root).parts
    cleaned_parts = [p for p in relative_parts if p != "generated"]
    return Path(*cleaned_parts)

def clean_directory(input_dir: Path, output_dir: Path) -> None:
        
    processed = 0
    copied = 0

    for md_file in input_dir.rglob("*.md"):
        # Always skip Hugo index files
        if md_file.name.lower() == "_index.md":
            continue
        output_path = output_dir / md_file.relative_to(input_dir)
        
            # 🔹 RULE: headless folders → copy as-is
        if is_under_headless(md_file, input_dir):

            # If under a "generated" folder, flatten it
            if "generated" in md_file.relative_to(input_dir).parts:
                relative_path = remove_generated_from_path(md_file, input_dir)
                output_path = output_dir / relative_path
            else:
                output_path = output_dir / md_file.relative_to(input_dir)

            copy_md_as_is(md_file, output_path)
            copied += 1
            continue


        # 🔹 Otherwise → clean
        raw = load_md_file(md_file)
        frontmatter, body = extract_frontmatter(raw)

        if is_layout_only(frontmatter, body):
            continue

        filtered_frontmatter = filter_frontmatter(frontmatter)
        cleaned_body = clean_markdown(body)
        rebuilt_md = rebuild_frontmatter(filtered_frontmatter) + cleaned_body

        save_clean_md(output_path, rebuilt_md)
        processed += 1

    print(f"✅ Cleaned files: {processed}")
    print(f"📦 Copied headless files: {copied}")
    print(f"📁 Total processed: {processed + copied}")
# -------------------------
#runner code

if __name__ == "__main__":

    # Paths:
    input_dir = Path("./documentation/raw")      # input folder
    output_dir = Path("./documentation/preprocessed")  # output folder

    print(f"Cleaning {input_dir} → {output_dir}")
    clean_directory(input_dir, output_dir)
    print(f"✅ Processed {len(list(output_dir.rglob('*.md')))} files")