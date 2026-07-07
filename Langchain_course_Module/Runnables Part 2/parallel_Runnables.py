from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# LLM
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# Output Parser
parser = StrOutputParser()

# Prompt 1
joke_prompt = PromptTemplate(
    template="Write a funny joke about {topic}.",
    input_variables=["topic"]
)

# Prompt 2
fact_prompt = PromptTemplate(
    template="Write 5 interesting facts about {topic}.",
    input_variables=["topic"]
)

# Chains
joke_chain = joke_prompt | model | parser
fact_chain = fact_prompt | model | parser

# Parallel Runnable
parallel_chain = RunnableParallel(
    joke=joke_chain,
    facts=fact_chain
)

# Run
result = parallel_chain.invoke(
    {
        "topic": "Artificial Intelligence"
    }
)

print(result)