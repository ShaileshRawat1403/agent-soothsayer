from pathlib import Path
from datetime import datetime

def write_dev_doc_markdown(data: dict, output_path: str) -> None:
    """
    Writes a structured Markdown dev_doc file using the provided dictionary.

    Args:
        data (dict): Keys like function_name, language, code, explanation, etc.
        output_path (str): Full file path to save the Markdown.
    """
    function_name = data.get("function_name", "unknown_function")
    language = data.get("language", "python")
    created_at = data.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    markdown = f'''---
function_name: {function_name}
language: {language}
mode: dev_doc
created_at: {created_at}
---

### 🧠 Function: {function_name}

```{language}
{data.get("code", "").strip()}
```

---

### 🔍 Explanation:

{data.get("explanation", "").strip()}

---

### 🧪 Usage Example:

```{language}
{data.get("example", "").strip()}
```

---

### ⏱️ Time Complexity:

{data.get("complexity", "").strip()}

---

### 💡 Insight:

{data.get("insight", "").strip()}

---

### ⚠️ Known Limitations:

{data.get("limitations", "").strip()}

---

### 🏷️ Tags:

{data.get("tags", "").strip()}
'''

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"[✅] Markdown written to: {output_path}")

if __name__ == "__main__":
    sample_data = {
        "function_name": "add_numbers",
        "language": "python",
        "code": "def add_numbers(a, b):\n    return a + b",
        "explanation": "Adds two numbers together.",
        "example": "print(add_numbers(2, 3))  # Output: 5",
        "complexity": "O(1)",
        "insight": "Direct addition, no loop.",
        "limitations": "Assumes numeric inputs only.",
        "tags": "math, utility"
    }

    write_dev_doc_markdown(sample_data, "output_docs/add_numbers.md")
