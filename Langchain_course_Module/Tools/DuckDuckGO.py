from langchain_community.tools import DuckDuckGoSearchRun

# Create the search tool
search = DuckDuckGoSearchRun()

# Search query
result = search.invoke("Latest AI news")

print(result)