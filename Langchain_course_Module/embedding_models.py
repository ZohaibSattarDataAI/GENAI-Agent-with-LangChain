from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for aggressive batting.",
    "MS Dhoni is a former Indian captain famous for finishing matches.",
    "Sachin Tendulkar is called the God of Cricket.",
    "Rohit Sharma is known for double centuries in ODI cricket.",
    "Jasprit Bumrah is a fast bowler known for yorkers and pace.",
    "Zohaib Sattar is the Data Scientist and AI Engineer at Data Science LimeoX.",
]

query = "tell me about Zohaib Sattar"

doc_embeddings = model.encode(documents)
query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding, doc_embeddings)[0]

index = scores.argmax()

print("Query:", query)
print("Best Match:", documents[index])
print("Score:", scores[index])