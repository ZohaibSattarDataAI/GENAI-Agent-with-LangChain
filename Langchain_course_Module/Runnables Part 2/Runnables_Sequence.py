from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

# Prompt 1
prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# Ollama Model
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# Output Parser
parser = StrOutputParser()

# Prompt 2
prompt2 = PromptTemplate(
    template="Explain the following joke:\n\n{text}",
    input_variables=["text"]
)

# Runnable Sequence
chain = RunnableSequence(
    prompt1,
    model,
    parser,
    prompt2,
    model,
    parser
)

# Invoke
result = chain.invoke(
    {
        "topic": "Artificial Intelligence"
    }
)

print(result)