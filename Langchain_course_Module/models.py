# from langchain_openai import OpenAI
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

llm = OllamaLLM(model='llama3', temperature=0.7, max_tokens=150)

result=llm.invoke("Write a short poem about the beauty of nature.")

print(result)