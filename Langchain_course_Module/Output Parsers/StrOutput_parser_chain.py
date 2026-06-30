from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Ollama Model
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.7
)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n{text}',
    input_variables=['text']
)

# Chain 1
chain1 = template1 | model

# Chain 2
chain2 = template2 | model

# Run Chain 1
result1 = chain1.invoke({'topic': 'black hole'})

# Run Chain 2
result2 = chain2.invoke({'text': result1.content})

print(result2.content)