from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



#1. Static Prompt

prompt = ChatPromptTemplate.from_template(
    "Explain AI in simple words."
)

messages = prompt.format_messages()


#2. Dynamic Prompt
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

messages = prompt.format_messages(topic="Machine Learning")

#ChatBase

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello"),
    AIMessage(content="Hi!"),
    HumanMessage(content="What is AI?")
]

# # response = chat.invoke(messages)
# print(response)



