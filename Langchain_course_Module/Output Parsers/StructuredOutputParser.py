from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Load Model
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# Response Schema
response_schemas = [
    ResponseSchema(
        name="Data Science",
        description="Top 3 programming languages for Data Science with one-line reason for each"
    ),
    ResponseSchema(
        name="Ethical Hacking",
        description="Top 3 programming languages for Ethical Hacking with one-line reason for each"
    ),
    ResponseSchema(
        name="Artificial Intelligence",
        description="Top 3 programming languages for Artificial Intelligence with one-line reason for each"
    )
]

# Create Parser
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Prompt
template = PromptTemplate(
    template="""
You are a career guidance expert.

Recommend the top 3 programming languages for the following fields:

1. Data Science
2. Ethical Hacking
3. Artificial Intelligence

{format_instructions}
""",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Chain
chain = template | model | parser

# Invoke
result = chain.invoke({})

print(result)