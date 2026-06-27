from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
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

prompt = ChatPromptTemplate.from_template(
    "Explain Artificial Intelligence in simple words."
)

messages = prompt.format_messages()

response = chat.invoke(messages)

print(response.content)