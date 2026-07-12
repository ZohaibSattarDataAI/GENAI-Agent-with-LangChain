from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
Analyze the sentiment of the text.

Respond in this format:

Sentiment: <Positive/Negative/Neutral>

Reason: <One sentence>

Text:
{text}
""")

chain = prompt | model

text = "I got addmission in AI i got job after completing 6 semester 12 internship experience and i am very happy to share this news with you"

response = chain.invoke({"text": text})

print(response.content)