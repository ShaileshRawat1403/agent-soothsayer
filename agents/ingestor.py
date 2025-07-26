from crewai import Agent, Task
from tools.parse_md_function import parse_dev_doc_markdown
from langchain_core.tools import tool  # Required for compatibility with CrewAI tool usage

@tool
def parse(file_path: str):
    """Parse a Markdown dev_doc file and return structured dictionary data."""
    return parse_dev_doc_markdown(file_path)

def IngestorAgent(llm):
    return Agent(
        role="Ingestor",
        goal="Read a Markdown dev_doc file and extract structured information.",
        backstory="You're a meticulous parser who ensures all markdown elements are converted to clean, usable data for downstream agents.",
        verbose=True,
        tools=[parse],
        llm=llm
    )

def IngestorTask(agent):
    return Task(
        description="Parse the markdown file at 'input_docs/add_numbers.md' and return its structured dictionary data.",
        expected_output="A dictionary with keys like function_name, code, explanation, etc.",
        agent=agent
    )
