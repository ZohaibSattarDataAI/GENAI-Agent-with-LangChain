from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# Prompt
prompt = PromptTemplate(
    template="""
You are an expert English grammar assistant.

Correct the grammar, spelling, and punctuation of the following text.

Only return the corrected text.

Text:
{text}
""",
    input_variables=["text"]
)

# Parser
parser = StrOutputParser()

# Chain
chain = prompt | llm | parser

# User Input
user_text = input("Enter your text: ")

# Generate
result = chain.invoke(
    {
        "text": user_text
    }
)

print("\nCorrected Text:\n")
print(result)