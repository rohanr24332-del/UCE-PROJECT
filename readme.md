# Unified Cognitive Engine (UCE)

Unified Cognitive Engine (UCE) is an experimental modular AI framework for structured task execution. It combines planning, reasoning, verification, and persistent memory into a multi-stage pipeline designed to solve a wide range of tasks using local large language models.

The project focuses on building a transparent and extensible cognitive architecture rather than a single conversational interface.

## Features

- **Task Planning** – Decomposes user requests into structured execution steps.
- **Multi-Agent Pipeline** – Coordinates specialized reasoning, research, coding, and critique agents.
- **Iterative Verification** – Reviews generated outputs and performs corrective reasoning when required.
- **Knowledge Memory** – Stores previous tasks and results for future retrieval and reuse.
- **Tool Execution** – Supports controlled execution of Python-based tasks.
- **Local LLM Integration** – Compatible with Ollama-hosted models such as DeepSeek, Llama, and Phi.
- **Offline Execution** – Runs entirely on local hardware without requiring cloud APIs.

## Architecture

```
User Request
      │
      ▼
 Task Planner
      │
      ▼
 Multi-Agent Execution
 ├── Research
 ├── Reasoning
 ├── Coding
 └── Critique
      │
      ▼
 Verification & Self-Correction
      │
      ▼
 Knowledge Memory
      │
      ▼
 Final Response
```

## Installation

Create a virtual environment and install the required dependencies:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install a local language model with Ollama:

```bash
ollama pull deepseek-r1:7b
```

Update `models/config.py`:

```python
USE_OLLAMA = True
DEFAULT_MODEL = "deepseek-r1:7b"
```

## Running

Interactive mode:

```bash
python main.py
```

Demo mode:

```bash
python main.py --demo
```

## Project Goals

UCE explores several components commonly found in modern AI agent systems:

- Structured task planning
- Multi-agent coordination
- Iterative reasoning
- Output verification
- Persistent knowledge storage
- Local model execution

The architecture is designed to be modular so that individual components can be extended or replaced independently.

## Current Status

The project currently includes:

- Planning pipeline
- Multi-agent execution
- Verification and self-correction
- Persistent knowledge memory
- Local LLM integration through Ollama

Future work includes richer memory retrieval, stronger constraint verification, improved tool usage, and more capable reasoning workflows.

## License

This project is intended for research, experimentation, and educational purposes.
