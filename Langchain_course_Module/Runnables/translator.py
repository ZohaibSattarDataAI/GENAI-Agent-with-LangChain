from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load LLM
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are a professional translator.

Translate the following English sentence into Urdu.

English:
{text}

Urdu:
""")

# Output Parser
parser = StrOutputParser()

# Runnable Chain
chain = prompt | model | parser

print("=" * 50)
print(" English to Urdu Translator ")
print("=" * 50)

while True:
    text = input("\nEnter English Sentence (type 'exit' to quit): ")

    if text.lower() == "exit":
        print("\nThank you!")
        break

    response = chain.invoke({
        "text": text
    })

    print("\nUrdu Translation:\n")
    print(response)