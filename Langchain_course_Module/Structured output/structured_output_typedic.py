from typing_extensions import TypedDict
from langchain_ollama import ChatOllama


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

# Structured Output
structured_llm = llm.with_structured_output(Person)

# Invoke Model
response = structured_llm.invoke(
    "My name is Ali. I am 22 years old and I live in Lahore."
)

print(response)