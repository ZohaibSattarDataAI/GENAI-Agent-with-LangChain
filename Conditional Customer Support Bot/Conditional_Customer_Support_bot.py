from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# Load Local LLM
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.3
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional Customer Support Assistant.

Responsibilities:
- Answer customer questions politely.
- Help users solve problems.
- Explain products and services.
- Respond professionally.
- If you don't know the answer, politely ask the customer to contact human support.
- Keep responses short and clear.
"""
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

history = []

print("=" * 60)
print("Customer Support Bot")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    question = input("\nCustomer: ")

    if question.lower() == "exit":
        print("\nBot: Thank you for contacting customer support!")
        break

    response = chain.invoke({
        "history": history,
        "question": question
    })

    print("\nSupport:", response)

    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=response))