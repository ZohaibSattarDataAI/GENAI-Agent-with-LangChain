from langchain_core.runnables import RunnableLambda

# Custom Function
def make_upper(text):
    return text.upper()

# RunnableLambda
chain = RunnableLambda(make_upper)

result = chain.invoke("artificial intelligence")

print(result)