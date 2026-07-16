from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

documents = [
    Document(page_content="Artificial Intelligence is the simulation of human intelligence by machines."),
    Document(page_content="Machine Learning is a subset of Artificial Intelligence."),
    Document(page_content="Deep Learning uses neural networks with multiple layers."),
    Document(page_content="Natural Language Processing enables computers to understand human language."),
    Document(page_content="Computer Vision allows computers to analyze images and videos.")
]

embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

vectorstore = Chroma.from_documents(
    documents,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,
        "fetch_k": 5
    }
)

docs = retriever.invoke("Explain AI")

for doc in docs:
    print(doc.page_content)