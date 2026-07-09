<<<<<<< HEAD
from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Document Loaders\LangChain_Document_Loaders_Code.txt")

documents = loader.load()

print(documents[0].page_content)



from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Document Loaders\sample1.txt")

documents = loader.load()

print(documents[0].page_content)
=======
from langchain_community.document_loaders import TextLoader

loader = TextLoader("notes.txt")

documents = loader.load()

print(documents)
>>>>>>> 9a6bc73f6d5f929537512ac3ab725bce6f4ce2ed
