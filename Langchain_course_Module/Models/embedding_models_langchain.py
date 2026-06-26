from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

documents = [
    "Virat Kohli is an Indian cricketer known for aggressive batting.",
    "MS Dhoni is a former Indian captain famous for finishing matches.",
    "Sachin Tendulkar is called the God of Cricket.",
    "Rohit Sharma is known for double centuries in ODI cricket.",
    "Jasprit Bumrah is a fast bowler known for yorkers and pace.",
    "Zohaib Sattar is the Data Scientist and AI Engineer at Data Science LimeoX.",
]

docs = [Document(page_content=text) for text in documents]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(docs, embeddings)

# Create Retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)

query = "tell me about virat & Zohaib"

results = retriever.invoke(query)

print("Query:", query)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(results, start=1):
    print(f"{i}. {doc.page_content}")