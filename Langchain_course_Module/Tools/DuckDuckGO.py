from langchain_community.tools import DuckDuckGoSearchRun

# Create search tool
search = DuckDuckGoSearchRun()

# Search
result = search.invoke("Python programming")

print(result)