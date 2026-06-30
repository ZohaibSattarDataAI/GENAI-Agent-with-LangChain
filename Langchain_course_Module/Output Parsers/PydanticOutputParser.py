from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

class Language(BaseModel):
    language: str = Field(description="Programming language name")
    creator: str = Field(description="Creator")
    year: int = Field(description="Release year")

parser = PydanticOutputParser(pydantic_object=Language)

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
        "question": "Tell me about Python programming language."
    }
)

print(result)