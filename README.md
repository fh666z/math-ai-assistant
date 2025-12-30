# Math AI Assistant

An AI-powered math assistant built with LangChain and Google's Gemini model. This project demonstrates how to use LangChain agents with custom tools for mathematical calculations.

## Features

- 🤖 Powered by Google Gemini 3 Flash Preview model
- 🔧 Built with LangChain ReAct agent framework
- 🛠️ Custom tools for number extraction and summation
- 📊 Handles both integers and decimal numbers
- 💬 Natural language math queries

## How It Works

The assistant uses a **ReAct (Reasoning + Acting) agent** that can:
1. Analyze your natural language query
2. Decide which tool to use
3. Execute the tool with appropriate parameters
4. Return a human-readable response

### Available Tools

| Tool | Description |
|------|-------------|
| `add_numbers` | Extracts and sums integers from text |
| `sum_decimal_numbers` | Extracts and sums all numbers including decimals |

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

Before running the application, you need to set up your Google API key:

1. Get your Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

2. Set the API key as an environment variable:

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

Alternatively, you can create a `.env` file in the project root (make sure to add it to `.gitignore`):

```
GOOGLE_API_KEY=your-api-key-here
```

## Usage

Run the math assistant:

```bash
python math-assistant.py
```

The script uses a sample query to demonstrate the agent's capabilities. You can modify the `query` variable in `math-assistant.py` to ask different math-related questions.

### Example Query

The default query calculates the total GDP:

```
In 2023, the US GDP was approximately $27.72 trillion, while Canada's was 
around $2.14 trillion and Mexico's was about $1.79 trillion what is the total.
```

The agent will:
1. Recognize this as a summation problem
2. Select the `sum_decimal_numbers` tool
3. Extract the numbers: 27.72, 2.14, 1.79
4. Return: "The sum is 31.65"

## Example Queries

- "Add 10, 20, and 30 together"
- "What is the sum of 15.5, 22.3, and 8.2?"
- "Calculate 100 + 200 + 300"
- "The prices are $19.99, $25.50, and $12.75. What's the total?"

## Project Structure

```
math-ai-assistant/
├── math-assistant.py    # Main application with agent and tools
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── LICENSE             # License information
```

## Code Overview

```python
# Define custom tools with @tool decorator
@tool
def add_numbers(text: str) -> str:
    """Adds integers extracted from the input text."""
    ...

@tool
def sum_decimal_numbers(text: str) -> str:
    """Extracts and sums all numbers including decimals."""
    ...

# Initialize agent with tools
agent = initialize_agent(
    tools=[add_numbers, sum_decimal_numbers],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Execute with invoke()
response = agent.invoke({"input": "Your query here"})
```

## Dependencies

- `langchain` - Framework for building LLM applications
- `langchain-google-genai` - Google Gemini integration for LangChain
- `langchain-core` - Core LangChain components
- `langchain-community` - Community-contributed LangChain integrations
- `wikipedia` - Wikipedia API wrapper
- `google-genai` - Google Generative AI SDK

## License

See the [LICENSE](LICENSE) file for details.

## Contributing

This is a training project for AI-assisted math calculations. Feel free to fork and modify for your own learning purposes.

## Notes

- Make sure to keep your API key secure and never commit it to version control
- The model used is `gemini-3-flash-preview` - check Google's documentation for the latest available models
- Rate limits may apply based on your Google API plan
- The agent uses `verbose=True` to show the reasoning process during execution
