import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from langchain_std_tools import search_wikipedia
from math_functions import (
    add_numbers, sum_decimal_numbers, sum_numbers_from_text,
    calculate_power, multiply_numbers, divide_numbers, subtract_numbers
)


# Use the selected Google Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Optional: can also be auto-detected from env
)

tools = [calculate_power]
agent = create_react_agent(
    model = llm,
    tools = tools,
    prompt = "You are a helpful assistant that can perform various mathematical operations. Use the tools precisely and explain your reasoning clearly.")

query = "What is 2 to the power of 10?"
response = agent.invoke({"messages": [("human", query)]})

for msg in response["messages"]:
    print(msg.content)