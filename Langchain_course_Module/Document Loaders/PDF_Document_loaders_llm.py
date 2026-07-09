from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# ---------------------------------------
# Load Ollama Model
# ---------------------------------------
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# ---------------------------------------
# Load PDF
# ---------------------------------------
loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)

documents = loader.load()

# Combine all pages into one document
pdf_text = "\n\n".join([doc.page_content for doc in documents])

# ---------------------------------------
# Prompt Template
# ---------------------------------------
prompt = ChatPromptTemplate.from_template("""
You are an expert AI assistant.

Read the following PDF carefully and generate:

1. A short summary (3-5 lines)
2. Key points in bullet form
3. Important skills or technologies mentioned (if any)

PDF Content:
{document}

Answer:
""")

# ---------------------------------------
# Create Chain
# ---------------------------------------
chain = prompt | llm

# ---------------------------------------
# Generate Summary
# ---------------------------------------
response = chain.invoke({"document": pdf_text})

# ---------------------------------------
# Output
# ---------------------------------------
print("=" * 80)
print("PDF SUMMARY")
print("=" * 80)
print(response.content)

print("\n" + "=" * 80)
print("PDF INFORMATION")
print("=" * 80)
print(f"Total Pages : {len(documents)}")

print("\nFirst Page Preview:\n")
print(documents[0].page_content[:1000])  # First 1000 characters