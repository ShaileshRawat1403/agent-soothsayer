---
title: Building Soothsayer
description: A comprehensive, thinking-first guide to building your own CrewAI-powered local AI agent for meaningful content and communication.
status: Stable
version: v1.1
maintainer: Shailesh Rawat (PoeticMayhem)
last_updated: 2025-07-27
tags: [agentic-ai, crewai, markdown-parser, gradio, ollama, langchain, internal-comms, thinking-loop, change-translation]

---

# 🧠 Building Soothsayer  
*A thinking assistant isn’t built in a day. It’s built in loops.*

---

## 📍 What Are We Building?

Soothsayer is not a chatbot.  
It’s a **modular, local-first, CrewAI-powered agentic system** designed to help you think clearly — and communicate meaningfully.

It transforms:
- Raw thoughts → Structured output  
- Unclear notes → Aligned documentation  
- Internal ambiguity → Sharable understanding  

You'll build an AI system that:
- Reads from structured Markdown inputs  
- Thinks using a philosophy-aligned system prompt  
- Breaks roles into modular agents (Parser → Clarifier → Scribe)  
- Runs fully offline using **Ollama + Mistral**  
- Delivers styled responses via **Gradio UI**

---

## 💻 System Requirements

| Requirement | Details |
|-------------|---------|
| OS          | macOS, Linux, or Windows (with WSL) |
| Python      | v3.10 or newer |
| RAM         | Minimum 8GB (Recommended: 16GB for LLMs) |
| Disk        | At least 3GB free for Ollama + models |
| LLM         | Ollama (`mistral` model) |
| Ports       | Port `7860` for local Gradio UI |

---

## 🧰 Tools Used

| Component      | Tool/Library         | Purpose |
|----------------|----------------------|---------|
| LLM Engine      | Ollama + Mistral     | Local model, no API key needed |
| Agentic Engine  | CrewAI               | Multi-agent orchestration |
| Prompt Parser   | Custom Markdown Parser | Extracts title, overview, and purpose |
| Language Framework | LangChain        | Prompt templating and chaining |
| UI              | Gradio (Blocks API) | Local browser-based interface |
| UI Styling      | Custom CSS          | Sans Serif Sentiments design |
| Containerization| Docker (optional)   | Portable deployment |
| Automation      | GitHub Actions      | CI/CD for Markdown and Python linting |

---

## 🔁 Thinking Loop: Ideate → Investigate → Iterate → Create

Soothsayer follows your system-level thinking framework.

| Phase       | Description |
|-------------|-------------|
| Ideate      | Receive messy or partial thoughts |
| Investigate | Identify what's missing or unclear |
| Iterate     | Refine structure and meaning |
| Create      | Generate a usable, aligned output |

---

## 📡 Agent Roles and Modular Thinking

| Agent         | Description | Thinking Phase |
|---------------|-------------|----------------|
| 🧾 Parser Agent     | Extracts metadata and context from `.md` file | Ideate |
| 🧠 Clarifier Agent  | Identifies ambiguity, checks for tone, intent gaps | Investigate + Iterate |
| ✍️ Scribe Agent     | Generates structured, clean, reusable response | Create |

Currently, all three roles are embedded into a **single Soothsayer agent**, but the system is designed to scale into **separate CrewAI agents** for modular reasoning.

---

## 📂 Folder Structure

```plaintext
soothsayer-crewai/
├── agents/
│   └── soothsayer_agent.py           # Reflective agent logic with embedded prompt structure
├── configs/
│   └── tools/
│       └── parse_md_function.py      # Markdown field extraction logic
├── input_docs/
│   └── add_numbers.md                # Sample structured input
├── gradio_ui/
│   └── app.py                        # Gradio Blocks UI for chat
├── requirements.txt                  # Python dependencies
├── Dockerfile                        # (Optional) container setup
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions for linting
├── BUILDING_SOOTHSAYER.md            # This file
└── TECH_STACK.md                     # Architecture, CI/CD, deployment

---

🧰 Step-by-Step Setup

Step 1: Clone the Repo

git clone https://github.com/your-username/soothsayer-crewai
cd soothsayer-crewai

Step 2: Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux

Step 3: Install Requirements

pip install -r requirements.txt

Ensure you have Ollama installed:
https://ollama.com

Pull the local LLM:

ollama pull mistral


---

📝 Create an Input Markdown File

Inside input_docs/, add a file:

add_numbers.md

---
Title: Add Numbers Utility
Overview: This function takes two integers and returns their sum.
Why It Matters: Helps simplify repeated addition tasks in our service layer.
---


---

🧠 Understanding the System Prompt

In soothsayer_agent.py, the Markdown is parsed into this form:

You are Soothsayer, an AI strategist built to translate complexity into clarity...
📘 Title: Add Numbers Utility
📎 Overview: This function takes two integers and returns their sum.
📌 Why It Matters: Helps simplify repeated addition tasks...

This forms the structured base for reasoning and generation.


---

🚀 Launch the App

cd gradio_ui
python app.py

Your browser will open with a clean Gradio interface where you can paste a messy thought and get structured output.


---

❌ Debugging the Journey (What Broke + Fixes)

🔸 Missing Prompt Values Error

Error: Please provide Prompt Values for: task, lazy_prompt
Fix: Removed unused lazy prompt argument. Used direct task string.


---

🔸 Agent Not Triggering

Error: Nothing returned, no Crew execution
Fix: Created a proper Crew object:

crew = Crew(
    agents=[soothsayer],
    tasks=[task],
    verbose=True
)


---

🔸 Markdown Crashes on NoneType

Cause: Missing fields like Overview
Fix: In parser, use safe access:

data.get("Overview", "")


---

📐 Architecture Flow (Single-Agent Mode)

[Markdown File]
     ↓
parse_dev_doc_markdown()
     ↓
System Prompt Assembly
     ↓
CrewAI Task → Soothsayer Agent
     ↓
Ollama Mistral LLM
     ↓
Response (Title, Overview, Why It Matters...)
     ↓
Gradio UI → Exportable Markdown


---

🧪 Sample Thought → Output

Input Thought:
"I need to document a small function that adds numbers, but also explain why it matters for service logic."

Agent Response:

📘 Title: Add Numbers Utility  
📎 Overview: This function takes two integers and returns their sum.  
📌 Why It Matters: This utility ensures consistency across internal service logic by avoiding repetition of arithmetic logic.


---

✍ Customizing the Agent Personality

To change tone, add guidance in soothsayer_agent.py:

You are Soothsayer, an AI strategist who speaks like a senior editor with a sharp eye for ambiguity and poetic style...

You can embed:

✨ Humor

🧾 Formality

🧠 Socratic prompts

🗣 Departmental tone (Legal, UX, PM, etc.)



---

🔗 Scaling to Multi-Agent Crew

You can split the logic into 3 CrewAI agents:

Agent	Task

Parser Agent	Parse Markdown and extract clean prompt fields
Clarifier Agent	Detect ambiguities, contradictions, missing metadata
Scribe Agent	Create usable output in structured, aligned tone


Then wire them into a multi-task Crew like:

crew = Crew(
    agents=[parser, clarifier, scribe],
    tasks=[task_parse, task_clarify, task_write],
    verbose=True
)


---

🧠 What You’ve Built

You’ve created an agentic content engine that:

Reflects your thinking structure

Outputs reusable, well-formed documentation

Helps others understand, not just read

Operates locally, privately, and ethically


This isn’t just prompt engineering.
This is thinking architecture.


---

🔗 Related Docs

TECH_STACK.md — Architecture, deployment, CI/CD

soothsayer_agent.py — Core system logic

parse_md_function.py — Markdown ingestion

app.py — Gradio interface logic



---

✍ Author

Shailesh Rawat (PoeticMayhem)
A system thinker translating ambiguity into alignment — one structured sentence at a time.


---



