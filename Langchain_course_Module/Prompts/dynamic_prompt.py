from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(

    "Explain {topic} In simple words"
)

messages = prompt.format_messages(topic="Artificial Intelligence")
print(messages)
