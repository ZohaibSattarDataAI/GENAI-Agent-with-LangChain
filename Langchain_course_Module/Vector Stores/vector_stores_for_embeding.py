import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# ----------------------------------------
# Load Ollama Embedding Model
# ----------------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# ----------------------------------------
# Movie Dataset
# ----------------------------------------

documents = [

    Document(
        page_content="Kick is an action movie starring Salman Khan.",
        metadata={"title": "Kick"}
    ),

    Document(
        page_content="Dilwale is a romantic movie starring Shah Rukh Khan.",
        metadata={"title": "Dilwale"}
    ),

    Document(
        page_content="Theri is an action thriller starring Vijay.",
        metadata={"title": "Theri"}
    ),

    Document(
        page_content="Wanted is an action movie starring Salman Khan.",
        metadata={"title": "Wanted"}
    ),

    Document(
        page_content="Tere Naam is a romantic drama starring Salman Khan.",
        metadata={"title": "Tere Naam"}
    )

]

# ----------------------------------------
# Project Path
# ----------------------------------------

BASE_DIR = r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Vector Stores"

DB_PATH = os.path.join(BASE_DIR, "vector_db", "movie_db")

# Create folders if they don't exist
os.makedirs(DB_PATH, exist_ok=True)

# ----------------------------------------
# Create Vector Database
# ----------------------------------------

vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("=" * 50)
print("✅ Vector Database Created Successfully")
print(f"📁 Database Location: {DB_PATH}")
print("=" * 50)