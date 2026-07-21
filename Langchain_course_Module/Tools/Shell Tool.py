from langchain_community.tools import ShellTool

shell = ShellTool()

result = shell.invoke("dir")      # Windows
# result = shell.invoke("ls")     # Linux/macOS

print(result)