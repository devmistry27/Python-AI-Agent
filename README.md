# Python AI Agent

AI-powered coding assistant that uses Gemini 2.5 Flash to interact with a Python codebase through function calling. Includes a calculator application as a demonstration project.

## Project Structure

```
.
├── calculator/                # Demo calculator application
│   ├── pkg/
│   │   ├── calculator.py      # Core calculator logic with operator precedence
│   │   └── render.py          # JSON output formatting
│   ├── main.py                # Calculator CLI entry point
│   └── tests.py               # Unit tests
├── functions/                 # Agent capabilities
│   ├── get_files_info.py      # List directory contents
│   ├── get_file_content.py    # Read file contents (max 10K chars)
│   ├── run_python_file.py     # Execute Python files with args
│   └── write_file.py          # Create/overwrite files
├── call_function.py           # Function dispatcher
├── config.py                  # Constants (MAX_CHARS, WORKING_DIR)
├── prompts.py                 # System instruction for agent
├── main.py                    # Agent CLI entry point
└── tests.py                   # Function validation tests
```

## Requirements

- Python 3.x
- `google-genai`
- `python-dotenv`

## Installation

### Install Dependencies

```bash
pip install google-genai python-dotenv
```

### Configure API Key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### AI Agent

**Basic Command:**

```bash
python main.py "your prompt here"
```

**Verbose Mode:**

```bash
python main.py "your prompt here" --verbose
```

**Examples:**

```bash
python main.py "List all files in the calculator directory"
python main.py "Run the calculator tests"
python main.py "Fix any bugs you find in calculator.py"
```

### Calculator Application

**Execute Calculator:**

```bash
cd calculator
python main.py "3 + 5"
python main.py "(3 + 5) * 2"
python main.py "2 * 3 - 8 / 2 + 5"
```

**Output Format:**

```json
{
  "expression": "3 + 5",
  "result": 8
}
```

### Testing

**Run Calculator Tests:**

```bash
cd calculator
python tests.py
```

**Run Agent Function Tests:**

```bash
python tests.py
```

## Agent Capabilities

The agent provides the following operations through function calling:

**File Operations:**
- List files and directories with size information
- Read file contents (truncated at 10,000 characters)
- Write or overwrite files within the working directory

**Python Execution:**
- Execute Python files with optional command-line arguments
- 30-second timeout for script execution

All operations are sandboxed to the configured `WORKING_DIR` for security.

## Calculator Features

**Supported Operations:**
- Basic arithmetic: `+`, `-`, `*`, `/`
- Operator precedence (multiplication/division before addition/subtraction)
- Parentheses support for grouping expressions
- Whitespace-agnostic tokenization

**Error Handling:**
- Division by zero detection
- Invalid token validation
- Mismatched parentheses detection

## Security

**File System Protection:**
- All file operations constrained to `WORKING_DIR` via path validation
- No access to parent directories or absolute paths outside working directory
- File read truncation at 10,000 characters

**Execution Safety:**
- Python execution timeout of 30 seconds
- Sandboxed execution environment

## Configuration

Modify `config.py` to adjust system parameters:

```python
MAX_CHARS = 10000           # Maximum characters to read from files
WORKING_DIR = "./calculator" # Sandboxed working directory
```

## Architecture

**Core Components:**
- `main.py` - Agent entry point and CLI interface
- `call_function.py` - Dispatches function calls from Gemini to Python implementations
- `prompts.py` - System instructions defining agent behavior
- `config.py` - Centralized configuration management

**Function Module:**
Each function in `functions/` directory implements a specific capability:
- File system operations (read, write, list)
- Python script execution with argument passing
- Integrated with Gemini's function calling API

**Calculator Package:**
Demonstrates a complete Python application that the agent can interact with:
- Modular design with separate logic and rendering layers
- Comprehensive test coverage
- CLI interface for standalone usage
