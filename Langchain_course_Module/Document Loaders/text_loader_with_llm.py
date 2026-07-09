from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Load Ollama Model
# -----------------------------
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

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
# Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_template("""
You are an expert AI assistant.

Read the following document carefully and generate a clear, concise summary.

Document:
{document}

Summary:
""")

# -----------------------------
# Create Chain
# -----------------------------
chain = prompt | llm

# -----------------------------
# Function to Generate Summary
# -----------------------------
def summarize(document):
    response = chain.invoke({"document": document})
    return response.content

# -----------------------------
# Summary of File 1
# -----------------------------
summary1 = summarize(text1)

print("=" * 70)
print("SUMMARY OF FILE 1")
print("=" * 70)
print(summary1)

# -----------------------------
# Summary of File 2
# -----------------------------
summary2 = summarize(text2)

print("\n" + "=" * 70)
print("SUMMARY OF FILE 2")
print("=" * 70)
print(summary2)

# -----------------------------
# Combined Summary
# -----------------------------
combined_summary = summarize(combined_text)

print("\n" + "=" * 70)
print("COMBINED SUMMARY")
print("=" * 70)
print(combined_summary)