from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from xml.etree.ElementTree import ParseError
import time
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
# Load English Transcript
# =====================================================

print("=" * 60)
print("Loading English Transcript...")
print("=" * 60)

try:

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = None

    # -------------------------------------------------
    # Try Manual English Transcript
    # -------------------------------------------------

    try:

        english_transcript = transcript_list.find_transcript(["en"])
        print("Manual English transcript found.")

        for attempt in range(3):

            try:

                transcript = english_transcript.fetch()

                if transcript:
                    break

            except ParseError:

                print(f"Retry {attempt + 1}/3")
                time.sleep(2)

    except:
        pass

    # -------------------------------------------------
    # Try Auto Generated English Transcript
    # -------------------------------------------------

    if transcript is None:

        try:

            english_transcript = transcript_list.find_generated_transcript(["en"])
            print("Auto-generated English transcript found.")

            for attempt in range(3):

                try:

                    transcript = english_transcript.fetch()

                    if transcript:
                        break

                except ParseError:

                    print(f"Retry {attempt + 1}/3")
                    time.sleep(2)

        except:
            pass

    # -------------------------------------------------

    if transcript is None:

        print("\nNo English transcript available.")
        sys.exit()

    print("\nTranscript Loaded Successfully!")
    print(f"Transcript Segments : {len(transcript)}")

except Exception as e:

    print("\nFailed to load transcript!")
    print(type(e).__name__)
    print(e)
    sys.exit()

# =====================================================
# Convert Transcript to Document
# =====================================================

text = " ".join(
    item["text"] for item in transcript
)

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
# Prompt Template
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
# Chat Interface
# =====================================================

print("\n" + "=" * 60)
print("         YouTube RAG Chatbot")
print("=" * 60)

print("""
Example Questions:

• What is this video about?
• Summarize the video.
• Explain the main idea.
• What are the key points?
• Who is the speaker?
• What examples were discussed?
• Explain this like I'm a beginner.

Type 'exit' to quit.
""")

# =====================================================
# Chat Loop
# =====================================================

while True:

    question = input("Your Question: ").strip()

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

    print("\n" + "-" * 70 + "\n")