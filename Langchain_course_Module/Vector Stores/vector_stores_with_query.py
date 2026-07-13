from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os

# -----------------------------
# Load Chat Model
# -----------------------------
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# -----------------------------
# Load Embedding Model
# -----------------------------
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# -----------------------------
# Movie Dataset
# -----------------------------
documents = [

    Document(
        page_content="""
        Kick is an action comedy movie starring Salman Khan.
        The story follows Devi Lal Singh, a thrill-seeker who enjoys living dangerously.
        The movie features action, comedy, romance, and high-energy adventure.
        """,
        metadata={
            "title": "Kick",
            "genre": "Action",
            "year": 2014
        }
    ),

    Document(
        page_content="""
        Dilwale is a romantic action drama starring Shah Rukh Khan and Kajol.
        The story revolves around two lovers whose families become rivals.
        The movie combines romance, comedy, action, and emotional family moments.
        """,
        metadata={
            "title": "Dilwale",
            "genre": "Romance",
            "year": 2015
        }
    ),

    Document(
        page_content="""
        Theri is a Tamil action thriller starring Vijay.
        The story follows a police officer who hides his identity to protect his daughter
        while fighting dangerous criminals.
        """,
        metadata={
            "title": "Theri",
            "genre": "Action",
            "year": 2016
        }
    ),

    Document(
        page_content="""
        Don No. 1 is an action movie featuring an undercover hero who takes on
        powerful criminals. The film includes action, suspense, crime, and drama.
        """,
        metadata={
            "title": "Don No. 1",
            "genre": "Action",
            "year": 2007
        }
    ),

    Document(
        page_content="""
        Wanted is an action thriller starring Salman Khan.
        The movie follows an undercover police officer infiltrating the criminal world
        to eliminate dangerous gangsters.
        """,
        metadata={
            "title": "Wanted",
            "genre": "Action",
            "year": 2009
        }
    ),

    Document(
        page_content="""
        Tere Naam is a romantic drama starring Salman Khan.
        It tells the emotional love story of Radhe and Nirjara.
        The movie explores love, sacrifice, heartbreak, and tragedy.
        """,
        metadata={
            "title": "Tere Naam",
            "genre": "Romance",
            "year": 2003
        }
    ),

    Document(
        page_content="""
        Dabangg is an action comedy starring Salman Khan as police officer Chulbul Pandey.
        The movie is filled with action, comedy, family drama, and romance.
        """,
        metadata={
            "title": "Dabangg",
            "genre": "Action",
            "year": 2010
        }
    ),

    Document(
        page_content="""
        Sultan is a sports drama starring Salman Khan.
        It follows the inspiring journey of a wrestler who returns to the ring
        after personal struggles.
        """,
        metadata={
            "title": "Sultan",
            "genre": "Sports Drama",
            "year": 2016
        }
    ),

    Document(
        page_content="""
        Bajrangi Bhaijaan is an adventure drama starring Salman Khan.
        It follows Pavan's mission to reunite a lost Pakistani girl with her family.
        The movie highlights humanity, friendship, and compassion.
        """,
        metadata={
            "title": "Bajrangi Bhaijaan",
            "genre": "Adventure Drama",
            "year": 2015
        }
    ),

    Document(
        page_content="""
        Chennai Express is an action comedy starring Shah Rukh Khan and Deepika Padukone.
        The story follows an unexpected journey filled with romance, comedy, and adventure.
        """,
        metadata={
            "title": "Chennai Express",
            "genre": "Action Comedy",
            "year": 2013
        }
    )

]

# -----------------------------
# Create Vector Database
# -----------------------------
db_path = "./movie_db"

if not os.path.exists(db_path):

    print("Creating Vector Database...")

    vector_db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=db_path
    )

    print("Database Created Successfully!")

else:

    print("Loading Existing Database...")

    vector_db = Chroma(
        persist_directory=db_path,
        embedding_function=embeddings
    )

print("Vector Database Created Successfully!")

# -----------------------------
# User Query
# -----------------------------
query = "Recommend me a science fiction movie about space."

# -----------------------------
# Similarity Search
# -----------------------------
results = vector_db.similarity_search(
    query,
    k=3
)

print("\nTop Matching Movies\n")

context = ""

for i, doc in enumerate(results, start=1):

    print(f"Movie {i}")
    print("Title :", doc.metadata["title"])
    print("Genre :", doc.metadata["genre"])
    print("Year  :", doc.metadata["year"])
    print("Description :", doc.page_content)
    print("-"*60)

    context += doc.page_content + "\n"

# -----------------------------
# Ask LLM using Retrieved Context
# -----------------------------
prompt = f"""
You are a movie recommendation assistant.

Context:
{context}

Question:
{query}

Answer:
"""

response = model.invoke(prompt)

print("\nLLM Response\n")
print(response.content)