from crewai import Agent, Task, Crew
from langchain_ollama import OllamaLLM
from rich.console import Console
from rich.markdown import Markdown
import readline  # for CLI input history
import os

# === Terminal Markdown Renderer ===
console = Console()

# === Soothsayer System Philosophy ===
soothsayer_prompt = """
You are Soothsayer — a cognitive strategist for communication clarity, content enablement, and meaningful automation.

You operate by this loop:
→ Ideate → Investigate → Iterate → Create

You do not mimic ChatGPT. You reflect a human system of structured insight.
Always respond in clean, clear text. Avoid exclamations or vague inspiration.
If answering a content question, follow Flavor and Function:
Friction → Bridge → Evidence → Implication → Action → Look Ahead

You are allowed to help with:
- Internal comms and change messaging
- Dev docs and explanation
- Python or markdown code generation
- Clarifying fuzzy goals
- Form creation and workflow building

Never break character. Never make assumptions about user intent.
Wait, investigate, clarify — then act.

Keep all output actionable and markdown-friendly.
"""

# === LLM Setup ===
llm = OllamaLLM(
    base_url="http://localhost:11434",
    model="ollama/mistral",
    temperature=0.3
)

# === Soothsayer Agent ===
soothsayer = Agent(
    name="Soothsayer",
    role="Cognitive AI Strategist for Content, Change, and Code",
    goal="To bridge the thinking–doing gap through structured reflection and clarity",
    backstory="Soothsayer decodes ideas and executes clarity in systems, code, and comms.",
    verbose=True,
    allow_delegation=False,
    tools=[],
    llm=llm,
    system_prompt=soothsayer_prompt
)

# === Interactive Loop Starts Here ===
def interactive_cli():
    console.print("\n🧠 [bold cyan]Soothsayer CLI[/bold cyan] — Think. Clarify. Create.\n")
    console.print("Type your question or task. Type [bold]exit[/bold] to quit.\n")

    while True:
        try:
            user_input = input("💬 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n👋 [bold red]Exiting Soothsayer.[/bold red]")
            break

        if user_input.lower() in {"exit", "quit"}:
            console.print("\n👋 [bold red]Session Ended.[/bold red]")
            break

        task = Task(
            description=user_input,
            expected_output="A markdown-friendly, structured, and helpful answer",
            agent=soothsayer
        )

        crew = Crew(
            agents=[soothsayer],
            tasks=[task],
            verbose=False
        )

        result = crew.kickoff()

        console.print("\n[🗣️ Soothsayer Says]:\n", style="bold green")
        console.print(Markdown(result.output if hasattr(result, "output") else str(result)))
        console.print("\n" + "-"*60)

if __name__ == "__main__":
    interactive_cli()
