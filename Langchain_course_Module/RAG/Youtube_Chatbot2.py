from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)

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

video_id = "Gfr50f6ZBvo"

# =====================================================
# Load YouTube Transcript
# =====================================================

try:

    transcript = YouTubeTranscriptApi.get_transcript(
        video_id,
        languages=["en"]
    )

    text = " ".join(
        item["text"] for item in transcript
    )

    print("Transcript Loaded Successfully!")

except TranscriptsDisabled:

    print("No captions available for this video.")
    exit()

except Exception as e:

    print(type(e).__name__)
    print(e)
    exit()

# =====================================================
# Create Document
# =====================================================

documents = [
    Document(page_content=text)
]

# =====================================================
# Split Documents
# =====================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks : {len(chunks)}")

# =====================================================
# Create Vector Store
# =====================================================

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":4}
)

# =====================================================
# Prompt
# =====================================================

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer ONLY using the provided transcript.

If the answer is not present in the transcript, reply exactly:

"I couldn't find that information in the video."

Transcript:
{context}

Question:
{question}
""")

# =====================================================
# Helper Function
# =====================================================

def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs
    )

# =====================================================
# Build RAG Chain
# =====================================================

parallel_chain = RunnableParallel(
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    }
)

parser = StrOutputParser()

main_chain = (
    parallel_chain
    | prompt
    | llm
    | parser
)

# =====================================================
# Chat Loop
# =====================================================

print("\n" + "=" * 60)
print("         YouTube RAG Chatbot (Ollama)")
print("=" * 60)

print("""
Example Questions

• What is this video about?
• Summarize the video.
• Explain the main topic.
• What are the key points?
• Who is speaking?
• Explain this video like I'm a beginner.

Type 'exit' to quit.
""")

while True:

    question = input("Your Question: ").strip()

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    if not question:
        continue

    answer = main_chain.invoke(question)

    print("\nAnswer:\n")
    print(answer)
    print("\n" + "-" * 70)