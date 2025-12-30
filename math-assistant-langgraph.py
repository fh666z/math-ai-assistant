import os, time
from langchain_google_genai import ChatGoogleGenerativeAI
from math_functions import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
from langgraph.prebuilt import create_react_agent

# Use the selected Google Gemini model
# Note: Using Gemini 2.5 instead of 3.x because Gemini 3 requires thought signatures
# for function calling, which LangGraph doesn't automatically handle yet.
# See: https://ai.google.dev/gemini-api/docs/thought-signatures
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Optional: can also be auto-detected from env
)
quota_limit_wait = 1 # seconds to wait between requests to prevent quota limit errors

available_tools = [add_numbers,subtract_numbers, multiply_numbers, divide_numbers]
available_tools_names = [tool.name for tool in available_tools]

# Create the agent with all tools
math_agent = create_react_agent(
    model=llm,
    tools=available_tools,
    # Optional: Add a system message to guide the agent's behavior
    prompt="You are a helpful mathematical assistant that can perform various operations. Use the tools precisely and explain your reasoning clearly."
)
"""
print("\n--- Testing DivideTool ---")
response = math_agent.invoke({
    "messages": [("human", "What is 25 divided by 4?")]
})
# Get the final answer
final_answer = response["messages"][-1].content
print(final_answer)
print("Prevent quota limit error by waiting 1 second")
time.sleep(quota_limit_wait)

print("\n--- Testing SubtractTool ---")
response_2 = math_agent.invoke({
    "messages": [("human", "Subtract 100, 20, and 10.")]
})
# Get the final answer
final_answer_2 = response_2["messages"][-1].content
print(final_answer_2)
print("Prevent quota limit error by waiting 1 second")
time.sleep(quota_limit_wait)


print("\n--- Testing MultiplyTool ---")
response = math_agent.invoke({
    "messages": [("human", "Multiply 2, 3, and four.")]
})
print("Agent Response:", response["messages"][-1].content)

print("Prevent quota limit error by waiting 1 second")
time.sleep(quota_limit_wait)

print("\n--- Testing DivideTool ---")
response = math_agent.invoke({
    "messages": [("human", "Divide 100 by 5 and then by 2.")]
})
print("Agent Response:", response["messages"][-1].content)
"""


# Test Cases
test_cases = [
    {
        "query": "Subtract 100, 20, and 10.",
        "expected": {"result": 70},
        "description": "Testing subtraction tool with sequential subtraction."
    },
    {
        "query": "Multiply 2, 3, and 4.",
        "expected": {"result": 24},
        "description": "Testing multiplication tool for a list of numbers."
    },
    {
        "query": "Divide 100 by 5 and then by 2.",
        "expected": {"result": 10.0},
        "description": "Testing division tool with sequential division."
    },
    {
        "query": "Subtract 50 from 20.",
        "expected": {"result": -30},
        "description": "Testing subtraction tool with negative results."
    }

]

correct_tasks = []
# Corrected test execution
for index, test in enumerate(test_cases, start=1):
    query = test["query"]
    expected_result = test["expected"]["result"]  # Extract just the value
    
    print(f"\n--- Test Case {index}: {test['description']} ---")
    print(f"Query: {query}")
    
    # Properly format the input
    response = math_agent.invoke({"messages": [("human", query)]})
    
    # Find the tool message in the response
    tool_name = None
    tool_message = None
    for msg in response["messages"]:
        if hasattr(msg, 'name') and msg.name in available_tools_names:
            tool_name = msg.name
            tool_message = msg
            break
    
    if tool_name:
        # Parse the tool result from its content
        import json
        tool_result = json.loads(tool_message.content)["result"]
        print(f"Tool Result: {tool_result}")
        print(f"Expected Result: {expected_result}")
        
        if tool_result == expected_result:
            print(f"✅ Test Passed: {test['description']}")
            correct_tasks.append(test["description"])
        else:
            print(f"❌ Test Failed: {test['description']}")
    else:
        print("❌ No tool was called by the agent")

print("\nCorrectly passed tests:", correct_tasks)