from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Load First Text File
# -----------------------------
loader = TextLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Document Loaders\LangChain_Document_Loaders_Code.txt",
    encoding="utf-8"
)

documents = loader.load()

text1 = documents[0].page_content

# -----------------------------
# Load Second Text File
# -----------------------------
loader1 = TextLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\GENAI-Agent-with-LangChain\Langchain_course_Module\Document Loaders\sample1.txt",
    encoding="utf-8"
)

documents1 = loader1.load()

text2 = documents1[0].page_content

# -----------------------------
# Combine both files
# -----------------------------
combined_text = text1 + "\n\n" + text2

# -----------------------------
# Load Ollama Model
# -----------------------------
llm = ChatOllama(
    model="llama3.2",   # Change model if needed
    temperature=0
)

# -----------------------------
# Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_template("""
You are an expert AI assistant.

Read the following document carefully and generate a concise summary.

Document:
{document}

Summary:
""")

# -----------------------------
# Create Chain
# -----------------------------
chain = prompt | llm

# -----------------------------
# Invoke Model
# -----------------------------
response = chain.invoke({
    "document": combined_text
})

print("=" * 60)
print("SUMMARY")
print("=" * 60)

print(response.content)