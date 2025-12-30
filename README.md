# Math AI Assistant

An AI-powered math assistant built with LangChain and Google's Gemini model. This project demonstrates how to use AI models for mathematical calculations and problem-solving assistance.

## Features

- 🤖 Powered by Google Gemini 3 Flash Preview model
- 🔧 Built with LangChain for easy integration
- 📊 AI-assisted mathematical calculations and problem-solving
- 💬 Interactive chat interface for math queries

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

The script will send a query to the Gemini model and display the response. You can modify the `message` variable in `math-assistant.py` to ask different math-related questions.

## Example Queries

- "What is tool calling in langchain?"
- "Solve the equation 2x + 5 = 15"
- "Calculate the derivative of x^2 + 3x + 1"
- "Explain the Pythagorean theorem"

## Project Structure

```
math-ai-assistant/
├── math-assistant.py    # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── LICENSE             # License information
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
