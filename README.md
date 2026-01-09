# Math AI Assistant

An AI-powered math assistant built with LangChain, LangGraph, and Google's Gemini models. This project demonstrates how to use AI agents with custom tools for mathematical calculations and information retrieval.

## Features

- 🤖 Powered by Google Gemini models (2.5 Flash & 3 Flash Preview)
- 🔧 Built with both LangChain and LangGraph agent frameworks
- 🛠️ Custom mathematical tools for various operations
- 🌐 Wikipedia integration for factual lookups
- 📊 Handles integers, decimals, and complex expressions
- 💬 Natural language math queries
- ✅ Built-in test cases for validation

## How It Works

The assistant uses **ReAct (Reasoning + Acting) agents** that can:
1. Analyze your natural language query
2. Decide which tool(s) to use
3. Execute tools with appropriate parameters
4. Chain multiple operations if needed
5. Return human-readable responses

## Project Structure

```
math-ai-assistant/
├── math_functions.py            # Core math tools module
├── lanchain_std_tools.py        # Standard tools (Wikipedia)
├── math-assistant-langchain.py  # LangChain agent implementation
├── math-assistant-langgraph.py  # LangGraph agent with tests
├── std-tools-langchain.py       # Combined math + Wikipedia agent
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── LICENSE                      # License information
```

## Available Tools

### Mathematical Tools (`math_functions.py`)

| Tool | Description | Example |
|------|-------------|---------|
| `add_numbers` | Extracts and sums integers from text | `"Add 10 20 30"` → `60` |
| `sum_decimal_numbers` | Extracts and sums numbers including decimals | `"$27.72 and $2.14"` → `29.86` |
| `sum_numbers_from_text` | Extracts numbers and returns sum as float | `"Numbers: 5, 10, 15"` → `30.0` |
| `subtract_numbers` | Sequential subtraction from first number | `"100, 20, 10"` → `70` |
| `multiply_numbers` | Calculates product of all numbers | `"2, 3, 4"` → `24` |
| `divide_numbers` | Sequential division from first number | `"100, 5, 2"` → `10.0` |
| `calculate_power` | Raises first number to power of second | `"2, 10"` → `1024` |

### Standard Tools (`lanchain_std_tools.py`)

| Tool | Description |
|------|-------------|
| `search_wikipedia` | Search Wikipedia for factual information about any topic |

## Script Descriptions

### `math-assistant-langchain.py`
Basic LangChain agent using `initialize_agent` with the "zero-shot-react-description" strategy. Uses Gemini 3 Flash Preview model for simple addition queries.

### `math-assistant-langgraph.py`
Advanced LangGraph implementation using `create_react_agent`. Features:
- All four basic math operations (add, subtract, multiply, divide)
- Built-in test suite with expected results
- Quota limit handling with delays
- Uses Gemini 2.5 Flash (due to thought signature requirements in Gemini 3)

### `std-tools-langchain.py`
Combined agent that integrates mathematical operations with Wikipedia search, enabling queries like:
- "What is the capital of France? What is its population? Divide by the population of the second largest city."
- "What is 2 to the power of 10?"

## Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini model access

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd math-ai-assistant
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Set up your Google API key before running any script:

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

### Run the basic LangChain agent:
```bash
python math-assistant-langchain.py
```

### Run the LangGraph agent with tests:
```bash
python math-assistant-langgraph.py
```

### Run the combined math + Wikipedia agent:
```bash
python std-tools-langchain.py
```

## Example Queries

### Addition/Summation
- "Add 10, 20, and 30 together"
- "What is the sum of 15.5, 22.3, and 8.2?"
- "In 2023, the US GDP was $27.72 trillion, Canada's was $2.14 trillion. What's the total?"

### Subtraction
- "Subtract 100, 20, and 10"
- "Subtract 50 from 20"

### Multiplication
- "Multiply 2, 3, and 4"
- "What is 5 times 6 times 7?"

### Division
- "Divide 100 by 5 and then by 2"
- "What is 25 divided by 4?"

### Power/Exponentiation
- "What is 2 to the power of 10?"
- "Calculate 3 raised to the 4th power"

### Combined with Wikipedia
- "What is the population of Tokyo? Multiply it by 2."

## Dependencies

| Package | Description |
|---------|-------------|
| `langchain` | Framework for building LLM applications |
| `langchain-google-genai` | Google Gemini integration for LangChain |
| `langchain-core` | Core LangChain components |
| `langchain-community` | Community-contributed integrations |
| `langgraph` | Graph-based agent orchestration framework |
| `wikipedia` | Wikipedia API wrapper |
| `google-genai` | Google Generative AI SDK |

## Model Notes

- **Gemini 3 Flash Preview**: Used in basic LangChain agent
- **Gemini 2.5 Flash**: Used in LangGraph agents (Gemini 3 requires [thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures) for function calling, which LangGraph doesn't automatically handle yet)

## License

See the [LICENSE](LICENSE) file for details.

## Contributing

This is a learning project for AI-assisted math calculations. Feel free to fork and modify for your own purposes.

## Notes

- Keep your API key secure and never commit it to version control
- Rate limits may apply based on your Google API plan
- The LangGraph agent includes delays between requests to prevent quota errors
- Use `verbose=True` in agents to see the reasoning process during execution
