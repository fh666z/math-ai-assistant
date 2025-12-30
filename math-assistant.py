import os, re
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent

@tool
def add_numbers(text: str) -> str:
    """Adds integers extracted from the input text and returns the sum as a string.
    
    Args:
        text: A string containing numbers to be summed.
        
    Returns:
        A string with the sum of all integers found in the input.
    """
    numbers = [int(x) for x in text.replace(",", "").split() if x.isdigit()]
    total = sum(numbers)
    return f"The sum is {total}"

@tool
def sum_decimal_numbers(text: str) -> str:
    """Extracts and sums all numbers including decimals from the input text.
    
    Args:
        text: A string containing numbers (integers or decimals) to be summed.
        
    Returns:
        A string with the sum of all numbers found in the input.
    """
    matches = re.findall(r'-?\d+(?:\.\d+)?', text)
    if not matches:
        return "No numbers found in input."
    try:
        numbers = [float(num) for num in matches]
        total = sum(numbers)
        return f"The sum is {total}"
    except Exception as e:
        return f"Error during summation: {str(e)}"

# Use the selected Google Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Optional: can also be auto-detected from env
)

# Initialize agent with tools
tools = [add_numbers, sum_decimal_numbers]
agent = initialize_agent(
    tools,
    llm, 
    agent="zero-shot-react-description", 
    verbose=True, 
    handle_parsing_errors=True)

# Now that tools return simple strings, the agent should only expect "input"
query = "In 2023, the US GDP was approximately $27.72 trillion, while Canada's was around $2.14 trillion and Mexico's was about $1.79 trillion what is the total."
response = agent.invoke({"input": query})

# Print the response
if isinstance(response, dict):
    # If response is a dict (from invoke), extract the output
    output = response.get("output", response)
    print("\nResponse:", output)
elif hasattr(response, 'content'):
    # If response has a content attribute
    print("\nResponse Content:", response.content)
else:
    # If response is a string or other type
    print("\nResponse:", response)

