from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "I am your AI Asistance tell me everything"),
        ("user", "Tell me about {topic}")
    ]
)

messages = prompt.format_messages(topic="Artificial Intelligence")

print(messages)