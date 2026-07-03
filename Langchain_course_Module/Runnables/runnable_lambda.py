from langchain_core.runnables import RunnableLambda

def greet(name):
    return f"Hello, {name}! Welcome to LangChain."

runnable = RunnableLambda(greet)

result = runnable.invoke("Zohaib")

print(result)