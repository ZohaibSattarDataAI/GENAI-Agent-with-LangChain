from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.2",
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0,
)

chat = ChatHuggingFace(llm=llm)

# Memory
chat_history = []

print("🤖 AI Chatbot with Memory")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Save user message
    chat_history.append(HumanMessage(content=user_input))

    # Send complete history
    response = chat.invoke(chat_history)

    print("AI:", response.content)

    # Save AI response
    chat_history.append(AIMessage(content=response.content))