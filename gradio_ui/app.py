import gradio as gr
from crewai import Agent, Task, Crew
from langchain_ollama import OllamaLLM
from configs.tools.parse_md_function import parse_dev_doc_markdown

# === 1. Load your parsed markdown doc ===
parsed_data = parse_dev_doc_markdown("input_docs/add_numbers.md")

# === 2. Define Soothsayer's system prompt using markdown fields ===
def get_system_prompt(data):
    return f"""
You are Soothsayer, an AI strategist built to translate complexity into clarity — not just in code or content, but in communication itself.

Your job is to:
- Reflectively reframe internal updates, product shifts, or abstract narratives into accessible, aligned, and resonant communication.
- Detect assumptions, ambiguity, and friction in how ideas are conveyed.
- Refine content using principles of cognitive design, emotional tone-matching, and systems thinking.

Use this structure as a lens — not a cage:

---
📘 Title: {data.get('Title', 'Untitled')}
📎 Overview: {data.get('Overview', '')}
📌 Why It Matters: {data.get('Why It Matters', '')}
🧠 Prerequisites: {data.get('Prerequisites', '')}
🔧 Tasks/Instructions: {data.get('Tasks/Instructions', '')}
📎 Tips: {data.get('Tips', '')}
🧯 Troubleshooting: {data.get('Troubleshooting', '')}
📚 Resources: {data.get('Resources', '')}
📅 Last Updated: {data.get('Last Updated', '')}
---

Wait for the user's intent. Don’t respond quickly — respond wisely.
"""

# === 3. Define the Soothsayer Agent ===
def get_agent():
    return Agent(
        name="Soothsayer",
        role="AI Strategist for Communication, Product Clarity, and Change Enablement",
        goal="Transform fragmented updates, shifting narratives, and product transitions into structured clarity that aligns thought and action.",
        backstory=(
            "Soothsayer is not a documentation tool — it’s a cognitive partner.\n\n"
            "Built for content enablers, product owners, and reflective communicators, Soothsayer dissects ambiguity and reassembles meaning.\n\n"
            "It bridges technical intent and human insight — shaping narratives that aren’t just clear, but consequential.\n\n"
            "Every prompt is a signal. Every response, a recalibration."
        ),
        allow_delegation=False,
        verbose=False,
        llm=OllamaLLM(model="mistral"),
        system_prompt=get_system_prompt(parsed_data)
    )

soothsayer_agent = get_agent()

# === 4. Core Interaction Function ===
def interact_with_soothsayer(user_input):
    task = Task(
        description=user_input,
        expected_output="Reflective, structured, and cognitively resonant output",
        agent=soothsayer_agent
    )
    crew = Crew(
        agents=[soothsayer_agent],
        tasks=[task],
        verbose=False
    )
    result = crew.kickoff()
    return str(result)

# === 5. Custom CSS Inspired by PruningMyPothos ===
custom_css = """
body {
    font-family: 'Helvetica Neue', sans-serif;
    background-color: #faf7f2;
    color: #1a1a1a;
}

h1, h2, h3 {
    font-family: 'DM Serif Display', serif;
    font-weight: 400;
    color: #2b2b2b;
    letter-spacing: -0.3px;
}

.gradio-container {
    border: 1px solid #e4dfd7;
    border-radius: 16px;
    padding: 32px;
    background-color: #fffdf9;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.05);
}

textarea {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    color: #333333;
    background-color: #f5f3ef;
    border-radius: 12px;
    padding: 16px;
    border: 1px solid #ddd2c4;
}

button {
    background-color: #242424 !important;
    color: #ffffff !important;
    font-weight: 600;
    font-size: 15px;
    border-radius: 8px;
    padding: 12px 22px;
    margin-top: 16px;
}

button:hover {
    background-color: #3a3a3a !important;
}

.output-textbox {
    background-color: #fffefc;
    font-family: 'Georgia', serif;
    font-size: 16px;
    line-height: 1.7;
    border-radius: 12px;
    padding: 20px;
    border: 1px solid #ddd0c4;
    color: #2c2c2c;
}
"""

# === 6. Gradio Interface ===
iface = gr.Interface(
    fn=interact_with_soothsayer,
    inputs=gr.Textbox(
        lines=4,
        placeholder="What should Soothsayer reframe, translate, or clarify today?",
        label="🎯 Ask Soothsayer"
    ),
    outputs=gr.Textbox(label="🗣️ Soothsayer Responds", elem_classes="output-textbox"),
    title="🧠 Soothsayer — Strategist for Change, Clarity & Communication",
    description=(
        "Not just a rewriter — a re-thinker.\n"
        "Soothsayer transforms raw updates, friction-filled memos, and product ambiguity into crisp, cognitively aligned clarity."
    ),
    css=custom_css,
    theme="default"
)

if __name__ == "__main__":
    iface.launch(share=True)
