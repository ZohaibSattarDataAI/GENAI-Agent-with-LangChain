from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -----------------------------------
# Load PDF
# -----------------------------------

loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)

documents = loader.load()

print(f"Total Pages: {len(documents)}")

# Combine all pages into one text
pdf_text = "\n\n".join(doc.page_content for doc in documents)

# -----------------------------------
# Load Ollama Model
# -----------------------------------

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# -----------------------------------
# Prompt Template
# -----------------------------------

prompt = ChatPromptTemplate.from_template("""
You are an AI assistant.

Answer the user's question ONLY using the information provided in the PDF below.

If the answer is not available in the PDF, reply:

"I couldn't find this information in the provided PDF."

PDF Content:
{context}

Question:
{question}
""")

# -----------------------------------
# Output Parser
# -----------------------------------

parser = StrOutputParser()

# -----------------------------------
# LangChain Chain
# -----------------------------------

chain = prompt | model | parser

# -----------------------------------
# Chat Loop
# -----------------------------------

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = chain.invoke({
        "context": pdf_text,
        "question": question
    })

    print("\nAnswer:\n")
    print(answer)