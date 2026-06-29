from typing_extensions import TypedDict
from langchain_ollama import ChatOllama
import time


# Define Output Schema
class Person(TypedDict):
    name: str
    age: int
    city: str


# Load Model
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=1.5
)
start = time.time()
# Structured Output
structured_llm = llm.with_structured_output(Person)

# Invoke Model
response = structured_llm.invoke(
    "My name is Ali. I am 22 years old and I live in Lahore."
)

end = time.time()

print(f"Time taken: {end - start} seconds")

print(response)
print(response.name)
print(response.age)
print(response.city)