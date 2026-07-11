from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)

documents = loader.load()

print(f"Total Pages: {len(documents)}")

# Recursive Character Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# Split the documents
split_documents = text_splitter.split_documents(documents)

print(f"\nTotal Chunks: {len(split_documents)}\n")

# Print each chunk
for i, doc in enumerate(split_documents, start=1):
    print(f"========== Chunk {i} ==========")
    print(doc.page_content)
    print(f"\nLength: {len(doc.page_content)}")
    print(f"Metadata: {doc.metadata}")
    print("-" * 80)