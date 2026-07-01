from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

prompt = PromptTemplate(
    template="Explain {topic} in simple words.",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic": "Data Science"
})

print(result)
chain.get_graph().print_ascii()