from typing_extensions import Final, TypedDict
from langchain_ollama import ChatOllama
import time


# Define Output Schema
class Person(TypedDict):
    overall_sentiment: str
    confidence_score: str
    positive_points: str
    negative_points: str
    final_summary: str

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
    """I recently purchased a new laptop for my university projects and programming work. At first, I was really impressed with its sleek design, lightweight body, and vibrant display. The keyboard is comfortable for long coding sessions, and the battery easily lasts around 7 to 8 hours, which is perfect for my daily routine. Setting up the laptop was quick, and most applications installed without any issues.

However, after using it for about three weeks, I started noticing several problems. The system becomes very slow whenever I run multiple applications at the same time. Even opening a web browser with several tabs and VS Code together causes noticeable lag. The cooling fan also gets surprisingly loud during normal usage, and the laptop becomes warm after only 20 to 30 minutes of work. On a few occasions, the system froze completely, forcing me to restart it.

The customer support team was polite and responded quickly, but they couldn't provide a permanent solution. They only suggested updating drivers and reinstalling Windows, which did not completely solve the performance issues.

Despite these problems, I still appreciate the display quality, battery life, and overall portability of the laptop. If the performance and heating issues were fixed, I would definitely recommend it to others. At the moment, I have mixed feelings because the laptop has several excellent features but also some frustrating limitations that affect my daily productivity."""
)

end = time.time()

print(f"Time taken: {end - start} seconds")

print(response)
print(response["overall_sentiment"])
print(response["confidence_score"])
print(response["positive_points"])
print(response["negative_points"])
print(response["final_summary"])