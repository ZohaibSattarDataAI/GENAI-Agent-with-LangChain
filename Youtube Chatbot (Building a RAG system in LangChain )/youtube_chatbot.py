from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import sys

# =====================================================
# Local LLM
# =====================================================

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# =====================================================
# Video ID
# =====================================================

video_id = "cFnqX6V21h4"

# =====================================================
# Load Transcript
# =====================================================

print("\nLoading transcript...\n")

try:

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = None

    # Try manual English transcript
    try:
        transcript = transcript_list.find_transcript(["en"]).fetch()
        print("English transcript found.")
    except:
        pass

    # Try auto-generated English transcript
    if transcript is None:
        try:
            transcript = transcript_list.find_generated_transcript(["en"]).fetch()
            print("Auto-generated English transcript found.")
        except:
            pass

    if transcript is None:
        print("No English transcript available.")
        sys.exit()

    if len(transcript) == 0:
        print("Transcript is empty.")
        sys.exit()

    text = " ".join(
        item["text"]
        for item in transcript
    )

    documents = [
        Document(page_content=text)
    ]

    print(f"Transcript Loaded Successfully!")
    print(f"Transcript Segments : {len(transcript)}")

except Exception as e:

    print("\nFailed to load transcript!")
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

print(f"\nTotal Chunks : {len(chunks)}")

# =====================================================
# Vector Store
# =====================================================

print("\nCreating Vector Store...")

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)

print("Vector Store Ready!")

# =====================================================
# Prompt
# =====================================================

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer ONLY using the provided transcript.

If the answer is not found in the transcript, reply exactly:

"I couldn't find that information in the video."

Transcript:
{context}

Question:
{question}
""")

chain = prompt | llm | StrOutputParser()

# =====================================================
# Chat Loop
# =====================================================

print("\n" + "=" * 60)
print("        YouTube RAG Chatbot")
print("=" * 60)

print("""
Example Questions

- What is this video about?
- Summarize the video.
- Explain the main topic.
- What examples were discussed?
- Who is the speaker?
- What is the conclusion?
- Give me important points.

Type 'exit' to quit.
""")

while True:

    question = input("\nYour Question: ").strip()

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    if question == "":
        continue

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

    print("\nAnswer:\n")
    print(answer)
    print("\n" + "-" * 70)