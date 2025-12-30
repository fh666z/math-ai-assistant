import re
from langchain_core.tools import tool

# List of tools exported by this module
__all__ = ["add_numbers", "sum_decimal_numbers", "sum_numbers_from_text"]


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

@tool
def sum_numbers_from_text(inputs: str) -> float:
    """
    Adds a list of numbers provided in the input string.
    
    Args:
        text: A string containing numbers that should be extracted and summed.
        
    Returns:
        The sum of all numbers found in the input.
    """
    # Use regular expressions to extract all numbers from the input
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]
    result = sum(numbers)
    return result

