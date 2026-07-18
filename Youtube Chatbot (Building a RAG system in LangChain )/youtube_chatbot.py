from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import sys

# =====================================================
# Load Local LLM
# =====================================================

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# =====================================================
# YouTube Video ID
# =====================================================

video_id = "cFnqX6V21h4"

# =====================================================
# Load Transcript
# =====================================================

print("Loading transcript...\n")

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join(
        item["text"] for item in transcript
    )

    documents = [
        Document(page_content=text)
    ]

    print("Transcript Loaded Successfully!")
    print(f"Total Transcript Segments: {len(transcript)}\n")

except Exception as e:
    print("Failed to load transcript.\n")
    print(type(e).__name__)
    print(e)
    sys.exit()

# =====================================================
# Split Documents
# =====================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

# =====================================================
# Create Vector Store
# =====================================================

print("\nCreating Vector Store...")

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)

print("Vector Store Ready!\n")

# =====================================================
# Prompt
# =====================================================

prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Answer ONLY using the provided YouTube transcript.

If the answer is not available in the transcript, reply exactly:

"I couldn't find that information in the video."

Transcript:
{context}

Question:
{question}
"""
)

chain = prompt | llm | StrOutputParser()

# =====================================================
# Chat Loop
# =====================================================

print("=" * 60)
print("      Chat with YouTube Video")
print("=" * 60)

print("\nYou can ask questions like:")
print("- What is this video about?")
print("- Summarize the video.")
print("- Explain the main topic.")
print("- What examples were discussed?")
print("- Who is the speaker?")
print("\nType 'exit' to quit.\n")

while True:

    question = input("Your Question: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    print("\nAnswer:\n")
    print(answer)
    print("\n" + "-" * 70 + "\n")