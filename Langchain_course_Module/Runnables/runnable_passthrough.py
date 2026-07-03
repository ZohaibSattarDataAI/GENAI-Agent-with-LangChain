from langchain_core.runnables import RunnablePassthrough

runnable = RunnablePassthrough()

result = runnable.invoke("Learning LangChain Runnables")

print(result)