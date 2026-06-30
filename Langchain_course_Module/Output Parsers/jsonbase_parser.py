from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
Return the answer in JSON format.

Question: {question}

Return:
{{
    "language": "...",
    "creator": "...",
    "year": "..."
}}
""",
    input_variables=["question"]
)

chain = template | model | parser

result = chain.invoke(
    {
        "question": "Tell me top 3 programming languages for AI , Datasceince or for ethical hacker"
    }
)

print(result)