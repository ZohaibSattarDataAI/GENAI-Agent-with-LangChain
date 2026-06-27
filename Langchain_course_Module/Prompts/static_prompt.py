from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Explain Artificial Intelligence in simple words."
)

messages = prompt.format_messages()
print(messages)