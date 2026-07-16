from langchain_community.document_loaders import WikipediaLoader
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# ----------------------------------
# Load Documents from Wikipedia
# ----------------------------------
loader = WikipediaLoader(
    query="Difference between ai agent and agentic ai or generative ai",
    load_max_docs=5
)

docs = loader.load()

print(f"Loaded {len(docs)} documents.\n")

# ----------------------------------
# Create Embedding Model
# ----------------------------------
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

# ----------------------------------
# Create Chroma Vector Store
# ----------------------------------
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Documents stored in Chroma.\n")

# ----------------------------------
# Create MMR Retriever
# ----------------------------------
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,
        "fetch_k": 10
    }
)

# ----------------------------------
# User Query
# ----------------------------------
query = "Explain Machine Learning"

results = retriever.invoke(query)

# ----------------------------------
# Display Results
# ----------------------------------
for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"Document {i}")
    print("=" * 80)

    print("Title :", doc.metadata.get("title"))
    print("Source:", doc.metadata.get("source"))

    print("\nContent:\n")
    print(doc.page_content[:700])
    print("\n")