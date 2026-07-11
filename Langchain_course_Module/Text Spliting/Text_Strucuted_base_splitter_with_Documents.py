from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)

documents = loader.load()

print(f"Total Pages: {len(documents)}")

# Recursive Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# Split documents
chunks = text_splitter.split_documents(documents)

print(f"\nTotal Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"========== Chunk {i} ==========")
    print(chunk.page_content)
    print(f"\nLength: {len(chunk.page_content)}")
    print(f"Metadata: {chunk.metadata}")
    print("-" * 80)