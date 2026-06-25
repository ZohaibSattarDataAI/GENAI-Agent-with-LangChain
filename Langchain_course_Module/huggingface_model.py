from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.2",
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0.7,
    # max_new_tokens=150
)

chat = ChatHuggingFace(llm=llm)

result = chat.invoke(
    "What is Data Science & AI? Write a short paragraph about it.Also list all skills required to become a Data Scientist or AI Engineer."
)
print(result.content)