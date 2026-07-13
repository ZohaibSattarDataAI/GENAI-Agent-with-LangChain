import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

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
print("✅ Existing Vector Database Loaded")
print("=" * 50)

# ----------------------------------------
# New Documents
# ----------------------------------------

new_documents = [

    Document(
        page_content="""
        Bajrangi Bhaijaan is an adventure drama starring Salman Khan.
        The movie follows Pavan as he helps a lost Pakistani girl
        reunite with her family.
        """,
        metadata={
            "title": "Bajrangi Bhaijaan",
            "genre": "Adventure",
            "year": 2015
        }
    ),

    Document(
        page_content="""
        Sultan is a sports drama starring Salman Khan.
        It tells the inspiring story of a wrestler who
        returns to the ring after personal struggles.
        """,
        metadata={
            "title": "Sultan",
            "genre": "Sports",
            "year": 2016
        }
    ),

    Document(
        page_content="""
        Chennai Express is an action comedy starring
        Shah Rukh Khan and Deepika Padukone.
        """,
        metadata={
            "title": "Chennai Express",
            "genre": "Comedy",
            "year": 2013
        }
    )

]

# ----------------------------------------
# Add Documents
# ----------------------------------------

vector_db.add_documents(new_documents)

print("\n✅ New Documents Added Successfully!")

# ----------------------------------------
# Test Similarity Search
# ----------------------------------------

query = input("\nSearch Movie: ")

results = vector_db.similarity_search(
    query,
    k=3
)

print("\nTop Matching Movies")
print("-" * 50)

for i, doc in enumerate(results, start=1):

    print(f"\nMovie {i}")
    print("Title :", doc.metadata["title"])

    if "genre" in doc.metadata:
        print("Genre :", doc.metadata["genre"])

    if "year" in doc.metadata:
        print("Year :", doc.metadata["year"])

    print("Description:")
    print(doc.page_content)

    print("-" * 50)