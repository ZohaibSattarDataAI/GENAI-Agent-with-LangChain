from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
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
# Load All PDFs from Directory
# ---------------------------------------
loader = DirectoryLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\FlyRankAI\Certifications",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

print(f"Total Pages Loaded: {len(documents)}")

# ---------------------------------------
# Combine all PDF pages
# ---------------------------------------
all_text = "\n\n".join([doc.page_content for doc in documents])

# ---------------------------------------
# Prompt Template
# ---------------------------------------
prompt = ChatPromptTemplate.from_template("""
You are an expert AI assistant.

Read the following PDF documents carefully and generate:

1. A concise summary.
2. Main topics covered.
3. Key points in bullet form.

Documents:
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
response = chain.invoke({"document": all_text})

# ---------------------------------------
# Print Summary
# ---------------------------------------
print("\n" + "=" * 80)
print("SUMMARY OF ALL PDF FILES")
print("=" * 80)
print(response.content)

# ---------------------------------------
# Show Loaded Documents
# ---------------------------------------
print("\n" + "=" * 80)
print("LOADED DOCUMENTS")
print("=" * 80)

for i, doc in enumerate(documents, start=1):
    print(f"\nPage {i}")
    print("Source :", doc.metadata["source"])
    print("Page   :", doc.metadata["page"])
    print(doc.page_content[:300])  # First 300 characters
    print("-" * 80)