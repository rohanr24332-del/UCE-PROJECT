Unified Cognitive Engine (UCE)
A Modular, Self-Improving, AGI-Inspired Multi-Agent Reasoning System

UCE is a research-grade AI architecture designed to simulate core components of early AGI systems.
It combines planning, multi-agent reasoning, verification, tool execution, and long-term memory into a single unified engine.

Unlike a regular chatbot, UCE performs structured cognitive workflows:

📌 Breaks tasks into actionable steps

📌 Uses multi-agent collaboration (planner, researcher, coder, critic)

📌 Self-verifies results and corrects mistakes

📌 Stores knowledge in long-term memory

📌 Uses local LLMs (DeepSeek / Llama) for offline reasoning

📌 Supports future extension toward AGI-like behaviour

UCE is fully modular, open-source, and runs locally on any machine with Ollama.

🧠 Key Features
✔ 1. Planning Engine

Uses a Planner module to break user tasks into structured sub-steps.

✔ 2. Multi-Agent System

Includes specialized agents that collaborate:

ResearchAgent – gathers insights

ReasonerAgent – solves each step

CoderAgent – writes & fixes code

CriticAgent – reviews correctness

✔ 3. Verification Loop

Each solution passes through an Iterative Verifier that:

Detects logical inconsistencies

Requests improvements

Re-runs reasoning

Produces stable, validated outputs

✔ 4. Knowledge Graph Memory

Stores and retrieves previous tasks, summaries, and compressed knowledge for future reasoning.

✔ 5. Tool Execution

Supports sandboxed Python code execution for validation and testing.

✔ 6. Local LLM Support (Offline Mode)

UCE integrates seamlessly with:

DeepSeek-R1 7B / 14B

Llama 3.1

Phi-3

running through Ollama, enabling offline AGI-like workflows.

✔ 7. Clean Console UI

Colored console output shows:

Step-by-step plans

Agent reasoning

Memory updates

Verification results

 Project Structure
UCE_full_final/
├── agents/
├── data/
├── memory/
├── models/
│   └── config.py
├── orchestrator/
├── planner/
├── reasoner/
├── tools/
├── utils/
├── verifier/
├── tests/
├── main.py
├── readme.md
└── requirements.txt

 Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/UCE.git
cd UCE

2️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install & configure Ollama

Download Ollama: https://ollama.com/download

Pull DeepSeek model:

ollama pull deepseek-r1:7b

🔌 Configuring Local LLM (DeepSeek)

Edit models/config.py:

USE_OLLAMA = True
OLLAMA_MODEL = "deepseek-r1:7b"

 Running UCE
Demo mode:
python main.py --demo

Interactive mode:
python main.py

 Example Output
---- ORCHESTRATOR ----
[Plan] Breaking task into steps...
[Reasoner] Solving step 1...
[Critic] Reviewing output...
[Verifier] VERIFIED
[Memory] Knowledge stored.


UCE produces verified, structured, and agent-coordinated reasoning steps — not generic chatbot responses.

 Why This Project Matters

UCE demonstrates several AGI-aligned concepts:

Multi-agent cognition

Self-correction

Knowledge storage and reuse

Modular reasoning

Offline LLM orchestration

Tool-based intelligence

This project is suitable for:

Research portfolios

AI/ML engineer job applications

Hackathons

AGI architecture studies

University final-year projects

🛠 Planned Upgrades

Knowledge graph visualizer

Context compression module

Autonomous multi-step task execution

Advanced coding agent

GUI dashboard

Plugin system for external tools

 Contributions

Pull requests are welcome!
This project is built to be modular and extensible.

 License

MIT License — free for personal and academic use.
