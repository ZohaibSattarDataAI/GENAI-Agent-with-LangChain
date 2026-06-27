from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
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

print("🤖 ChatBot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = chat.invoke(user_input)

    print("AI:", response.content)