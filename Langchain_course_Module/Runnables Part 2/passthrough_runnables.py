from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

parser = StrOutputParser()

joke_prompt = PromptTemplate.from_template(
    "Write a joke about {topic}"
)

explain_prompt = PromptTemplate.from_template(
    """
Explain this joke:

{joke}
"""
)

joke_chain = joke_prompt | model | parser

explain_chain = explain_prompt | model | parser

# Step 1: Keep topic + Generate joke
step1 = RunnableParallel(
    topic=RunnablePassthrough(),
    joke=joke_chain
)

# Step 2: Explain joke
chain = (
    step1
    | {
        "topic": lambda x: x["topic"],
        "joke": lambda x: x["joke"],
        "explanation": explain_chain
    }
)

result = chain.invoke("AI")

print(result)