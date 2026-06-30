from langchain_ollama import ChatOllama
import time

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

start = time.time()

response = llm.invoke("What is AI? Give a 2-line answer.")

end = time.time()

print(response.content)
print(f"\nTime Taken: {end - start:.2f} seconds")