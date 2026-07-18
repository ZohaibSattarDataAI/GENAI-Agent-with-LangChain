from langchain_community.retrievers import WikipediaRetriever
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# Step 1: Retrieve documents from Wikipedia
retriever = WikipediaRetriever(
    top_k_results=2,
    doc_content_chars_max=1000
)

docs = retriever.invoke("Artificial Intelligence")

# Step 2: Use Ollama Embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

# Step 3: Store documents in Chroma Vector Store
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Documents stored successfully!")