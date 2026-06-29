from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
import time

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is Machine Learning?")
]

start = time.time()

response = llm.invoke(messages)

end = time.time()

print(response.content)
print(f"\nTime Taken: {end - start:.2f} seconds")