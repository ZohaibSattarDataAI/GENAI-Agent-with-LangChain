from langchain_tavily import TavilySearch

search = TavilySearch(max_results=3)

result = search.invoke("Latest AI news")

print(result)