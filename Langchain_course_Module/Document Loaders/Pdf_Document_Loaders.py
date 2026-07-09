from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Load Ollama Model
# -----------------------------
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)


# Load first PDF file
loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)


documents = loader.load()

# -----------------------------
# Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_template("""
You are an expert AI assistant.

Read the following document carefully and generate a clear, concise summary.

Document:
{document}

Summary:
""")

# -----------------------------
# Create Chain
# -----------------------------
chain = prompt | llm

# -----------------------------
# Function to Generate Summary
# -----------------------------
def summarize(document):
    response = chain.invoke({"document": document})
    return response.content

# -----------------------------
# Summary of File 1
# -----------------------------
summary1 = summarize(text1)

print("=" * 70)
print("SUMMARY OF FILE 1")
print("=" * 70)
print(summary1)

# -----------------------------
# Summary of File 2
# -----------------------------
summary2 = summarize(text2)

print("\n" + "=" * 70)
print("SUMMARY OF FILE 2")
print("=" * 70)
print(summary2)

# -----------------------------
# Combined Summary
# -----------------------------
combined_summary = summarize(combined_text)

print("\n" + "=" * 70)
print("COMBINED SUMMARY")
print("=" * 70)
print(combined_summary)

print("===== File 1 =====")
print(documents[0].page_content)
print(len(documents))