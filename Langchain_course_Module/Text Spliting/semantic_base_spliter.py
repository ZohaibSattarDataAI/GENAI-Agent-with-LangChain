from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import SemanticChunker
from langchain_ollama import OllamaEmbeddings

# Load PDF
loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)

documents = loader.load()

# Ollama Embedding Model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Semantic Chunker
text_splitter = SemanticChunker(embeddings)

# Split Documents
chunks = text_splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"========== Chunk {i} ==========")
    print(chunk.page_content)
    print(chunk.metadata)
    print("-" * 80)