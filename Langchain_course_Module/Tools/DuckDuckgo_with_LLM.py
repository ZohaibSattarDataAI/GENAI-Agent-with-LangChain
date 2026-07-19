from langchain_community.tools import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama

search_tool = DuckDuckGoSearchRun()

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

llm_with_tools = model.bind_tools([search_tool])

response = llm_with_tools.invoke(
    "What is the latest version of Python?"
)

print(response)