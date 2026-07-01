from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

parser = StrOutputParser()

explain_chain = (
    PromptTemplate.from_template("Explain {topic}.")
    | model
    | parser
)

advantages_chain = (
    PromptTemplate.from_template("Write 5 advantages of {topic}.")
    | model
    | parser
)

parallel_chain = RunnableParallel(
    explanation=explain_chain,
    advantages=advantages_chain
)

result = parallel_chain.invoke({
    "topic": "Ethical Hacking"
})

print(result["explanation"])
print()
print(result["advantages"])

parallel_chain.get_graph().print_ascii()