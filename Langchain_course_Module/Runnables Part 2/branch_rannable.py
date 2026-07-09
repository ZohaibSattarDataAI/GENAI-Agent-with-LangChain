from langchain_core.runnables import RunnableBranch

def positive(x):
    return "Positive Number"

def negative(x):
    return "Negative Number"

branch = RunnableBranch(
    (lambda x: x > 0, positive),
    (lambda x: x < 0, negative),
    lambda x: "Zero"
)

# print(branch.invoke(10))
print(branch.invoke(-5))
# print(branch.invoke(0))