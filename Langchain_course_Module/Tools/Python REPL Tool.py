from langchain_experimental.tools import PythonREPLTool

python_tool = PythonREPLTool()

result = python_tool.invoke("print(25 + 5)")

print(result)