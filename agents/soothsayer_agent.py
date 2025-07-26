from crewai import Agent, Task, Crew
from langchain_ollama import OllamaLLM
from configs.tools.parse_md_function import parse_dev_doc_markdown

# === Load and parse the input Markdown file ===
input_path = "input_docs/add_numbers.md"
parsed_data = parse_dev_doc_markdown(input_path)

# === Prepare structured components from parsed Markdown ===
function_name = parsed_data.get("function_name", "")
language = parsed_data.get("language", "")
code = parsed_data.get("code", "")
explanation = parsed_data.get("explanation", "")
example = parsed_data.get("example", "")
complexity = parsed_data.get("complexity", "")
insight = parsed_data.get("insight", "")
limitations = parsed_data.get("limitations", "")
tags = parsed_data.get("tags", "")

# === Construct system prompt ===
soothsayer_system_prompt = f"""
You are Soothsayer — a cognitive strategist built for communication clarity, content enablement, and enterprise change.

Your task is to analyze and improve the following structured function documentation. Your response should:
- Improve insight, explanation, and known limitations
- Preserve original structure
- Think like a communicator, not just a coder
- Bridge the gap between what’s written and what’s understood

ONLY RETURN AN UPDATED PYTHON DICTIONARY with keys:
function_name, language, code, explanation, example, complexity, insight, limitations, tags

Do not use markdown or extra commentary.

--- START OF ORIGINAL FUNCTION DOC ---
Function Name: {function_name}
Language: {language}

Code:
{code}

Explanation:
{explanation}

Example:
{example}

Time Complexity:
{complexity}

Insight:
{insight}

Known Limitations:
{limitations}

Tags:
{tags}
--- END ---
"""

# === Define the Soothsayer Agent ===
soothsayer = Agent(
    name="Soothsayer",
    role="AI Strategist for Internal Comms, Product Clarity & Change Translation.",
    goal="Reflectively translate change communication, content strategy, and product documentation into clear, impactful, and psychologically resonant narratives.",
    backstory=(
        "Built to bridge the thinking–technical gap across communication, change, and content systems — "
        "Soothsayer reflects a strategist’s mind with the precision of structured reasoning."
    ),
    allow_delegation=False,
    verbose=True,
    tools=[],
    llm=OllamaLLM(
        base_url="http://localhost:11434",
        model="mistral",
        temperature=0.3
    ),
    system_prompt=soothsayer_system_prompt
)

# === Define initial doc task ===
improve_doc_task = Task(
    description="Improve the explanation, insight, and limitations in the function documentation",
    expected_output="An improved Python dictionary containing the updated doc fields",
    agent=soothsayer
)

# === Run batch doc improvement ===
print("\n📘 [Batch Mode] Running documentation improvement task...\n")
crew = Crew(
    agents=[soothsayer],
    tasks=[improve_doc_task],
    verbose=True
)
batch_response = crew.kickoff()

print("\n[🔮 Soothsayer Enhanced Output Dictionary]")
print(batch_response)

# === Optional: Interactive Mode ===
while True:
    user_input = input("\n💬 Ask Soothsayer (or type 'exit'): ")
    if user_input.lower() == "exit":
        print("👋 Exiting interactive mode.")
        break

    dynamic_task = Task(
        description=user_input,
        expected_output="Short helpful reply",
        agent=soothsayer
    )

    crew = Crew(
        agents=[soothsayer],
        tasks=[dynamic_task],
        verbose=False
    )
    chat_response = crew.kickoff()
    print("\n[🗣️ Soothsayer Says]:")
    print(chat_response)
