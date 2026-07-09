from langchain_community.document_loaders import TextLoader

# Load first text file
loader = TextLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Document Loaders\LangChain_Document_Loaders_Code.txt"
)

documents = loader.load()

print("===== File 1 =====")
print(documents[0].page_content)


# Load second text file
loader1 = TextLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Document Loaders\sample1.txt"
)

documents1 = loader1.load()

print("\n===== File 2 =====")
print(documents1[0].page_content)