# Python AI Agent

A modular Python-based AI agent system designed to perform code analysis, file operations, and Python script execution through function calling and structured workflows.

## Project Structure

```
PYTHON AI AGENT/
│
├── calculator/
│   ├── pkg/
│   │   ├── calculator.py
│   │   ├── render.py
│   │   ├── lorem.txt
│   │   ├── morelorem.txt
│   │   ├── main.py
│   │   └── __pycache__/
│   └── tests.py
│
├── functions/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   ├── write_file.py
│   └── __pycache__/
│
├── .env
├── .gitignore
├── .python-version
├── call_function.py
├── config.py
├── main.py
├── prompts.py
├── pyproject.toml
├── README.md
├── tests.py
└── uv.lock
```

## Features

**File Operations**
- Retrieve detailed metadata about project files
- Read and write file contents dynamically

**Function Orchestration**
- Centralized function dispatching through `call_function.py`
- Dynamic invocation of helper modules

**Python Execution**
- Programmatic execution of Python scripts
- Modular calculator package demonstrating extensible design

**AI Integration**
- Compatible with LLM APIs (Gemini, GPT) for autonomous agent behavior
- Structured prompts and configuration management

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/python-ai-agent.git
cd python-ai-agent
```

### Virtual Environment Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### Dependencies

Using `uv`:

```bash
uv sync
```

Using `pip`:

```bash
pip install -r requirements.txt
```

### Environment Configuration

Create `.env` file in root directory:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Basic Execution

```bash
python main.py
```

### Run Specific Python File

```bash
python functions/run_python_file.py
```

### Testing

```bash
pytest
```

## Architecture

**Core Components**
- `main.py` - Agent initialization and entry point
- `call_function.py` - Function dispatcher and orchestrator
- `config.py` - Configuration management
- `prompts.py` - Agent prompt templates

**Functions Module**
- `get_file_content.py` - File content retrieval
- `get_files_info.py` - File metadata extraction
- `run_python_file.py` - Python script execution
- `write_file.py` - File writing operations

**Calculator Package**
- Modular example demonstrating package integration
- Includes rendering, I/O operations, and testing

## Technical Stack

- **Language:** Python 3.10+
- **Key Libraries:** `dotenv`, `google-genai`, `uv`, `pytest`
- **Architecture:** Modular and extensible design
- **Application:** AI-driven automation and code manipulation

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/feature-name`)
5. Open Pull Request

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Roadmap

- OpenAI and Gemini model integration for enhanced reasoning
- Persistent memory for agent state management
- Expanded plugin system for additional functionality
- Comprehensive logging and error tracing
