from pathlib import Path
from configs.tools.parse_md_function import parse_dev_doc_markdown
from configs.tools.write_md_function import write_dev_doc_markdown

def run_conversion(input_file: str, output_file: str):
    """
    Parses a dev_doc markdown file and regenerates it using the writer.
    
    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the regenerated output Markdown file.
    """
    print(f"[🔍] Parsing: {input_file}")
    parsed_data = parse_dev_doc_markdown(input_file)

    if parsed_data:
        print(f"[✍️ ] Writing new version to: {output_file}")
        write_dev_doc_markdown(parsed_data, output_file)
    else:
        print("[❌] Could not parse input file.")

# 🔧 CLI support
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python core/runner.py <input_markdown_path> <output_markdown_path>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        run_conversion(input_path, output_path)
