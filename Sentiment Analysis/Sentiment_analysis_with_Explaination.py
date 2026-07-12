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

text = "The service was okay, but delivery was very late."

response = chain.invoke({"text": text})

print(response.content)