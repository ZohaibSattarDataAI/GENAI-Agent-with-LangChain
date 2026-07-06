from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# -----------------------------
# PDF Path
# -----------------------------
pdf_path = r"C:\Users\ZohaibSattar_Data_AI\Downloads\100_plus_programs_master_python.pdf"

print("\nLoading PDF...")

loader = PyPDFLoader(pdf_path)
documents = loader.load()

print(f"Loaded {len(documents)} pages")


# -----------------------------
# Split Documents
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


# -----------------------------
# Embeddings
# -----------------------------
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("Creating Vector Store...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)

print("Vector Store Ready!")


# -----------------------------
# LLM
# -----------------------------
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
"""
You are an expert AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply exactly:

I couldn't find that information in the PDF.

Context:
{context}

Question:
{question}
"""
)

parser = StrOutputParser()

chain = prompt | llm | parser


print("\n===================================")
print("PDF Chatbot Ready")
print("Type 'exit' to quit")
print("===================================\n")


while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    print("\nAssistant:")
    print(answer)
    print("-" * 80)