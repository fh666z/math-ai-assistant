import os
from langchain_google_genai import ChatGoogleGenerativeAI
from math_functions import sum_numbers_from_text

from langgraph.prebuilt import create_react_agent

# Use the selected Google Gemini model
# Note: Using Gemini 2.5 instead of 3.x because Gemini 3 requires thought signatures
# for function calling, which LangGraph doesn't automatically handle yet.
# See: https://ai.google.dev/gemini-api/docs/thought-signatures
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Optional: can also be auto-detected from env
)

agent_exec = create_react_agent(model=llm, tools=[sum_numbers_from_text])
msgs = agent_exec.invoke({"messages": [("human", "Add the numbers -10, -20, -30")]})


print(msgs["messages"][-1].content)