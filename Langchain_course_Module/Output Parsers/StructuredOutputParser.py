from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

response_schemas = [
    ResponseSchema(name="language", description="Programming language name"),
    ResponseSchema(name="creator", description="Creator of the language"),
    ResponseSchema(name="year", description="Release year")
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template="""
Answer the question.

{format_instructions}

Question:
{question}
""",
    input_variables=["question"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke(
    {
        "question": "Tell me about Python."
    }
)

print(result)