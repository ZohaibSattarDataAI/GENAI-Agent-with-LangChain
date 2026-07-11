from langchain_community.document_loaders import PyPDFLoader

# Load first PDF file
loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)


documents = loader.load()

print("===== File 1 =====")
print(documents[0].page_content)
print(len(documents))