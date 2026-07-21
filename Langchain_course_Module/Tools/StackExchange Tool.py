from langchain_community.tools import StackExchangeTool
from langchain_community.utilities import StackExchangeAPIWrapper

api_wrapper = StackExchangeAPIWrapper()

tool = StackExchangeTool(api_wrapper=api_wrapper)

result = tool.invoke("Python list comprehension")

print(result)