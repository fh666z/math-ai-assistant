import re
from langchain_core.tools import tool

# List of tools exported by this module
__all__ = ["add_numbers", "sum_decimal_numbers", "sum_numbers_from_text", 
    "multiply_numbers", "divide_numbers", "subtract_numbers", "calculate_power"]


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

@tool
def subtract_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string, negates the first number, and successively subtracts 
    the remaining numbers in the list.

    This function is designed to handle input in string format, where numbers are separated 
    by spaces, commas, or other delimiters. It parses the string, extracts valid numeric values, 
    and performs a step-by-step subtraction operation starting with the first number negated.

    Parameters:
    - inputs (str): 
      A string containing numbers to subtract. The string may include spaces, commas, or 
      other delimiters between the numbers.

    Returns:
    - dict: 
      A dictionary containing the key "result" with the calculated difference as its value. 
      If no valid numbers are found in the input string, the result defaults to 0.

    Example Input:
    "100, 20, 10"

    Example Output:
    {"result": -130}

    Notes:
    - Non-numeric characters in the input are ignored.
    - If the input string contains only one valid number, the result will be that number negated.
    - Handles a variety of delimiters (e.g., spaces, commas) but does not validate input formats 
      beyond extracting numeric values.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]

    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Start with the first number negated
    result = numbers[0]

    # Subtract all subsequent numbers
    for num in numbers[1:]:
        result -= num

    return {"result": result}

# Multiplication Tool
@tool
def multiply_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates their product.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the product of the numbers.

    Example Input:
    "2, 3, 4"

    Example Output:
    {"result": 24}

    Notes:
    - If no numbers are found, the result defaults to 1 (neutral element for multiplication).
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]
    print(numbers)

    # If no numbers are found, return 1
    if not numbers:
        return {"result": 1}

    # Calculate the product of the numbers
    result = 1
    for num in numbers:
        result *= num
        print(num)

    return {"result": result}


# Division Tool
@tool
def divide_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates the result of dividing the first number 
    by the subsequent numbers in sequence.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the quotient.

    Example Input:
    "100, 5, 2"

    Example Output:
    {"result": 10.0}

    Notes:
    - If no numbers are found, the result defaults to 0.
    - Division by zero will raise an error.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]


    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Calculate the result of dividing the first number by subsequent numbers
    result = numbers[0]
    for num in numbers[1:]:
        result /= num

    return {"result": result}


@tool
def calculate_power(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates the power of the first number to the second number.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the power of the first number to the second number.

    Example Input:
    "2, 3"

    Example Output:
    {"result": 8}

    Notes:
    - If no numbers are found, the result defaults to 0.
    - The first number is the base and the second number is the exponent.
    """
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]
    if not numbers:
        return {"result": 0}
    result = numbers[0] ** numbers[1]
    return {"result": result}

