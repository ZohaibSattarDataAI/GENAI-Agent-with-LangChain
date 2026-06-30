from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

# Load Ollama Model
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.7
)

# Create Prompt
prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI assistant.

    Answer the following question:

    {question}
    """
)

# Create Output Parser
output_parser = StrOutputParser()

# Create Chain
chain = prompt | llm | output_parser

# Invoke Chain
response = chain.invoke(
    {
        "question": "Explain Artificial Intelligence in simple words."
    }
)

print(response)