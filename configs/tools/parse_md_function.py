import re
from pathlib import Path
from typing import Dict, Optional


def parse_dev_doc_markdown(file_path: str) -> Optional[Dict[str, str]]:
    """
    Parses a structured dev_doc Markdown file and returns a dictionary of its components.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        dict: Parsed data with keys like function_name, language, code, explanation, etc.
    """
    if not Path(file_path).exists():
        print(f"[ERROR] File not found: {file_path}")
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    parsed_data = {}

    # Metadata (YAML frontmatter)
    meta_match = re.search(
        r"---\s*\nfunction_name:\s*(.+?)\s*\nlanguage:\s*(.+?)\s*\nmode:\s*(.+?)\s*\ncreated_at:\s*(.+?)\s*\n---",
        content,
        re.DOTALL
    )
    if meta_match:
        parsed_data["function_name"] = meta_match.group(1).strip()
        parsed_data["language"] = meta_match.group(2).strip()
        parsed_data["mode"] = meta_match.group(3).strip()
        parsed_data["created_at"] = meta_match.group(4).strip()

    # Sections
    def extract_section(title: str, code_block: bool = False):
        pattern = rf"###\s*{re.escape(title)}:\s*\n(?:```[^\n]*\n)?(.*?)(?:```)?\n(?:\n|###|\Z)"
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else ""

    parsed_data["code"] = extract_section("🧠 Function", code_block=True)
    parsed_data["explanation"] = extract_section("🔍 Explanation")
    parsed_data["example"] = extract_section("🧪 Usage Example", code_block=True)
    parsed_data["complexity"] = extract_section("⏱️ Time Complexity")
    parsed_data["insight"] = extract_section("💡 Insight")
    parsed_data["limitations"] = extract_section("⚠️ Known Limitations")
    parsed_data["tags"] = extract_section("🏷️ Tags")

    return parsed_data


# 🔧 CLI/Test usage
if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        print("Usage: python parse_md_function.py <path_to_markdown_file>")
    else:
        result = parse_dev_doc_markdown(sys.argv[1])
        print(json.dumps(result, indent=2, ensure_ascii=False))
