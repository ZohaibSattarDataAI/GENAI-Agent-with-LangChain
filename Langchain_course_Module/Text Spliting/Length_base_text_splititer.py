from langchain.text_splitter import CharacterTextSplitter

# Long sample text
text = """
Artificial Intelligence (AI) is transforming the way people live and work.
It is being used in healthcare to diagnose diseases, in finance to detect fraud,
in education to provide personalized learning, and in transportation to develop
self-driving cars. Machine Learning is a branch of AI that enables computers to
learn from data without being explicitly programmed. Deep Learning, a subset of
Machine Learning, uses neural networks with multiple layers to solve complex
problems such as image recognition, speech recognition, and natural language
processing. As technology continues to evolve, AI is expected to play an even
greater role in automation, decision-making, and scientific research. However,
ethical concerns such as privacy, bias, transparency, and job displacement must
also be addressed to ensure responsible use of Artificial Intelligence.
"""

# Length-based Text Splitter
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=50
)

# Split text into chunks
chunks = splitter.split_text(text)

# Print results
print(f"Total Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"========== Chunk {i} ==========")
    print(chunk)
    print(f"\nLength: {len(chunk)} characters")
    print("-" * 60)