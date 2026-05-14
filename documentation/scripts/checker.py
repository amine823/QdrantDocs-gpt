import re
from pathlib import Path
from collections import defaultdict


# -------------------------
# Patterns to flag
# -------------------------


CHECKS = {
    "image_left": re.compile(r"!\[.*?\]\(.*?\)"),
    "markdown_link_left": re.compile(r"\[.+?\]\(.+?\)"),
    "html_tag_left": re.compile(r"<[^>]+>"),
    "raw_url_left": re.compile(r"https?://\S+"),
    "double_space": re.compile(r" {2,}"),
    "orphan_dash": re.compile(r"(?<=\s)-(?=\s)"),
    "empty_heading": re.compile(r"^#{1,6}\s*$", re.MULTILINE),
}


CODE_FENCE = "```"


# -------------------------
# Helpers
# -------------------------


def split_code_blocks(text: str):
    """
    Yield (is_code, block_text, line_offset) where line_offset is start line of block
    """
    parts = text.split(CODE_FENCE)
    line_offset = 0
    
    for i, part in enumerate(parts):
        lines = part.splitlines(keepends=True)
        block_lines = len(lines)
        yield i % 2 == 1, part, line_offset
        line_offset += block_lines
    
    # Handle final part if even number of fences
    if len(parts) % 2 == 0:
        yield False, parts[-1], line_offset


def find_matches_with_lines(block: str, pattern: re.Pattern, start_line: int) -> list:
    """Find matches and return (line_num, line_content, match)"""
    matches = []
    for line_num, line in enumerate(block.splitlines(), start=start_line + 1):
        for match in pattern.finditer(line):
            matches.append((line_num, line.strip(), match.group()))
    return matches


# -------------------------
# File checker
# -------------------------


def check_file(path: Path) -> dict:
    report = defaultdict(list)
    text = path.read_text(encoding="utf-8", errors="ignore")
    
    total_lines = len(text.splitlines())
    
    # --- Code block integrity ---
    fence_count = text.count(CODE_FENCE)
    if fence_count % 2 != 0:
        report["unclosed_code_block"].append("Odd number of ```")
    
    # --- Scan non-code content ---
    for is_code, block, line_offset in split_code_blocks(text):
        if is_code:
            if "[URL]" in block:
                report["placeholder_in_code"].append("[URL] found in code block")
            continue
        
        # Check each pattern
        for name, pattern in CHECKS.items():
            matches = find_matches_with_lines(block, pattern, line_offset)
            for line_num, line_content, match_text in matches:
                report[name].append(f"Line {line_num}: '{line_content}' → '{match_text}'")
    
    # --- File-level checks ---
    if len(text.strip()) < 200:
        report["too_short"].append("File < 200 chars")
    
    if not re.search(r"^#{1,3}\s+", text, re.MULTILINE):
        report["no_headings"].append("No headings found")
    
    return dict(report)

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
# -------------------------
# Directory checker
# -------------------------


def check_directory(input_dir: Path):
    full_report = {}
    for md_file in input_dir.rglob("*.md"):
        if is_under_headless(md_file, input_dir):
            continue
        issues = check_file(md_file)
        if issues:
            full_report[str(md_file)] = issues
    
    return full_report


# -------------------------
# Reporter
# -------------------------


def print_report(report: dict):
    if not report:
        print("✅ No issues found")
        return
    
    print("⚠️ Issues detected:\n")
    
    for file_path, issues in report.items():
        print(f"📄 {file_path}")
        for issue_type, details in issues.items():
            print(f"  ❌ {issue_type}:")
            for detail in details:
                print(f"     {detail}")
        print()


# -------------------------
# Runner
# -------------------------


if __name__ == "__main__":
    preprocessed_dir = Path("./documentation/preprocessed")
    report = check_directory(preprocessed_dir)
    print_report(report)
