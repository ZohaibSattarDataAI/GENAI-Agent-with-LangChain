from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Load all PDF files from the folder
loader = DirectoryLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\FlyRankAI",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# Load documents
documents = loader.load()

# Total pages loaded
print(f"Total Documents (Pages): {len(documents)}")

# Show information about each page
for i, doc in enumerate(documents, start=1):
    print("=" * 60)
    print(f"Document/Page: {i}")
    print("Source:", doc.metadata["source"])
    print("Page:", doc.metadata["page"])
    print("Characters:", len(doc.page_content))