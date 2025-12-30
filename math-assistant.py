from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

# Use the selected Google Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Optional: can also be auto-detected from env
)

# Create the message
message = HumanMessage(content="What is tool calling in langchain?")

# Invoke the model
response = llm.invoke([message])

# Print the response
print("\nResponse Content:", response.content)