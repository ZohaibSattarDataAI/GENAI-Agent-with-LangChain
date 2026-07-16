from langchain_core.documents import Document
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

# ------------------------------------
# Create Sample Documents
# ------------------------------------
documents = [
    Document(page_content="""
    Artificial Intelligence (AI) is the simulation of human intelligence by machines.
    AI includes Machine Learning, Deep Learning, Computer Vision, Robotics,
    Expert Systems, and Natural Language Processing.
    """),

    Document(page_content="""
    Machine Learning is a subset of Artificial Intelligence.
    It enables systems to learn from data without explicit programming.
    Common algorithms include Linear Regression, Decision Trees, and Random Forest.
    """),

    Document(page_content="""
    Deep Learning is a subset of Machine Learning.
    It uses artificial neural networks with multiple hidden layers.
    It is widely used in image recognition and NLP.
    """),

    Document(page_content="""
    Python is one of the most popular programming languages
    for Artificial Intelligence and Machine Learning because
    of libraries such as NumPy, Pandas, TensorFlow, and PyTorch.
    """)
]

# ------------------------------------
# Embedding Model
# ------------------------------------
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

# ------------------------------------
# Create Vector Store
# ------------------------------------
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings
)

# ------------------------------------
# Base Retriever
# ------------------------------------
base_retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# ------------------------------------
# Local LLM
# ------------------------------------
llm = ChatOllama(
    model="qwen2.5:1.5b"
)

# ------------------------------------
# Create Compressor
# ------------------------------------
compressor = LLMChainExtractor.from_llm(llm)

# ------------------------------------
# Contextual Compression Retriever
# ------------------------------------
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# ------------------------------------
# User Query
# ------------------------------------
query = "Explain Machine Learning."

# Retrieve compressed documents
results = compression_retriever.invoke(query)

# ------------------------------------
# Print Results
# ------------------------------------
for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"Compressed Document {i}")
    print("=" * 80)
    print(doc.page_content)
    print()