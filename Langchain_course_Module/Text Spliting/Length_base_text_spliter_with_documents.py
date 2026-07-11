from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

# Load PDF
loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)

documents = loader.load()

print(f"Total Pages: {len(documents)}")

# Length-Based Text Splitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap=100
)

# Split the loaded documents
chunks = text_splitter.split_documents(documents)

print(f"\nTotal Chunks: {len(chunks)}\n")

# Display all chunks
for i, chunk in enumerate(chunks, start=1):
    print(f"========== Chunk {i} ==========")
    print(chunk.page_content)
    print(f"\nLength: {len(chunk.page_content)} characters")
    print("-" * 80)