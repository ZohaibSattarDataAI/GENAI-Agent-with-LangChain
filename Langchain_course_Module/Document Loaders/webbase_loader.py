from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    "https://python.langchain.com/"
)

documents = loader.load()

print("Total Documents:", len(documents))
print(documents[0].page_content[:1000])   # First 1000 characters
print(documents[0].metadata)