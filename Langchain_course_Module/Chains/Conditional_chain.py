from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

parser = StrOutputParser()

short_chain = (
    PromptTemplate.from_template(
        "Give a short explanation of {topic}."
    )
    | model
    | parser
)

detailed_chain = (
    PromptTemplate.from_template(
        "Give a detailed explanation of {topic}."
    )
    | model
    | parser
)

branch = RunnableBranch(
    (
        lambda x: len(x["topic"]) > 10,
        detailed_chain
    ),
    short_chain
)

result = branch.invoke({
    "topic": "Artificial Intelligence"
})

print(result)
branch.get_graph().print_ascii()