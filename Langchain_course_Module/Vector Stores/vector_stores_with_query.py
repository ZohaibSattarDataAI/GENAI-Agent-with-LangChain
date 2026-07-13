import os
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma

# ----------------------------------------
# Load Chat Model
# ----------------------------------------

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# ----------------------------------------
# Load Embedding Model
# ----------------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# ----------------------------------------
# Vector Database Path
# ----------------------------------------

BASE_DIR = r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Vector Stores"

DB_PATH = os.path.join(BASE_DIR, "vector_db", "movie_db")

# ----------------------------------------
# Load Existing Vector Database
# ----------------------------------------

vector_db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

print("=" * 50)
print("✅ Vector Database Loaded Successfully")
print("=" * 50)

# ----------------------------------------
# Chat Loop
# ----------------------------------------

while True:

    query = input("\n🎬 Ask About Movies (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # -----------------------------
    # Similarity Search
    # -----------------------------

    results = vector_db.similarity_search(
        query,
        k=3
    )

    print("\nTop Matching Movies")
    print("-" * 50)

    context = ""

    for i, doc in enumerate(results, start=1):

        print(f"{i}. {doc.metadata['title']}")
        print(doc.page_content)
        print("-" * 50)

        context += doc.page_content + "\n"

    # -----------------------------
    # Prompt for LLM
    # -----------------------------

    prompt = f"""
You are an intelligent movie recommendation assistant.

Use ONLY the context provided below to answer the user's question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = model.invoke(prompt)

    print("\n🤖 AI Response")
    print("=" * 50)
    print(response.content)
    print("=" * 50)