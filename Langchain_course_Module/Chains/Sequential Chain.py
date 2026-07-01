from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

parser = StrOutputParser()

# First Prompt
explain_prompt = PromptTemplate(
    template="Explain {topic} in detail.",
    input_variables=["topic"]
)

explain_chain = explain_prompt | model | parser

# Second Prompt
summary_prompt = PromptTemplate(
    template="Summarize this in 5 bullet points:\n\n{text}",
    input_variables=["text"]
)

summary_chain = summary_prompt | model | parser

# Sequential Execution
explanation = explain_chain.invoke({
    "topic": "Machine Learning"
})

summary = summary_chain.invoke({
    "text": explanation
})

print(summary)
summary_chain.get_graph().print_ascii()