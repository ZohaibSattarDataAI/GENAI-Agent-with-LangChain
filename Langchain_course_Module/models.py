from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)

response = llm.invoke(
    "Write a Python function to reverse a string."
)

print(response.content)