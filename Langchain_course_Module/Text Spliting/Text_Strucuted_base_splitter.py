from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# Artificial Intelligence

Artificial Intelligence is transforming industries.

## Machine Learning

Machine Learning is a subset of AI.

### Supervised Learning

Supervised Learning uses labeled data.

### Unsupervised Learning

Unsupervised Learning finds hidden patterns.

## Deep Learning

Deep Learning uses neural networks.

# Applications

AI is used in healthcare, finance, education, and robotics.
"""

headers_to_split_on = [
    ("#", "Heading 1"),
    ("##", "Heading 2"),
    ("###", "Heading 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = markdown_splitter.split_text(markdown_text)

print(f"Total Chunks: {len(documents)}\n")

for i, doc in enumerate(documents, start=1):
    print(f"========== Chunk {i} ==========")
    print(doc.page_content)
    print("\nMetadata:")
    print(doc.metadata)
    print("-" * 80)