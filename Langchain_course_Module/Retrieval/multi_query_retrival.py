from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever

# -----------------------------
# LLM
# -----------------------------
llm = ChatOllama(
    model="qwen2.5:1.5b"
)

# -----------------------------
# Embedding Model
# -----------------------------
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

# -----------------------------
# Load Existing Chroma Database
# -----------------------------
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# -----------------------------
# Multi Query Retriever
# -----------------------------
retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=llm
)

# -----------------------------
# User Query
# -----------------------------
query = "Explain Artificial Intelligence"

# Retrieve Documents
docs = retriever.invoke(query)

# -----------------------------
# Print Results
# -----------------------------
for i, doc in enumerate(docs, start=1):
    print("=" * 80)
    print(f"Document {i}")
    print("=" * 80)

    print("Title :", doc.metadata.get("title"))
    print("Source:", doc.metadata.get("source"))

    print("\nContent:\n")
    print(doc.page_content[:700])
    print("\n")