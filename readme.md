🚀 Unified Cognitive Engine (UCE)

UCE is a modular, AGI-inspired reasoning system that uses planning, multi-agent collaboration, verification, and long-term memory to solve complex tasks.
It acts as a structured, self-correcting AI pipeline — far more organized than a normal chatbot.

⭐ Key Features

🧠 Planning Engine – breaks tasks into clear steps

🤖 Multi-Agent System – Research, Reasoning, Coding & Critic agents

✔️ Self-Verification Loop – detects mistakes and improves outputs

🧩 Knowledge Memory – stores summarized insights for reuse

🔧 Tool Execution – sandboxed Python code testing

🦾 Local LLM Support – works with DeepSeek, Llama, Phi via Ollama

💻 Offline & Free – runs entirely on your laptop

📁 Project Structure
UCE/
 ├── agents/
 ├── planner/
 ├── reasoner/
 ├── verifier/
 ├── orchestrator/
 ├── memory/
 ├── tools/
 ├── main.py
 ├── requirements.txt
 └── models/config.py

⚙️ Installation
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Install local LLM (example: DeepSeek-R1 7B)
ollama pull deepseek-r1:7b


Update models/config.py:

USE_OLLAMA = True
OLLAMA_MODEL = "deepseek-r1:7b"

▶️ Run Demo
python main.py --demo

📌 About

UCE is designed as a research-style AI system demonstrating structured cognition, multi-agent reasoning, and self-improvement workflows inspired by early AGI architectures.
