from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

parser = StrOutputParser()

story_prompt = PromptTemplate(
    template="Write a short story about {topic}.",
    input_variables=["topic"]
)

poem_prompt = PromptTemplate(
    template="Write a beautiful poem about {topic}.",
    input_variables=["topic"]
)

story_chain = story_prompt | model | parser
poem_chain = poem_prompt | model | parser

parallel = RunnableParallel(
    story=story_chain,
    poem=poem_chain
)

result = parallel.invoke(
    {
        "topic": "Nature"
    }
)

print("Story:\n")
print(result["story"])

print("\n" + "="*50 + "\n")

print("Poem:\n")
print(result["poem"])