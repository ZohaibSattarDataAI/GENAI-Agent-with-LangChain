from langchain_community.tools import RequestsGetTool

tool = RequestsGetTool()

print(tool.invoke("https://github.com/ZohaibSattarDataAI"))