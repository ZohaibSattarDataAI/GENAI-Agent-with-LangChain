from concurrent.futures import ThreadPoolExecutor

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are an HR Expert.

Analyze the following job description and provide:

1. Job Title
2. Required Skills
3. Experience
4. Education
5. Responsibilities
6. Technologies
7. Salary (if available)
8. Summary

Job Description:
{job}
""")

parser = StrOutputParser()

chain = prompt | model | parser

jobs = [
    """
    We are hiring a Python Developer.
    Skills: Python, Django, SQL
    Experience: 2 Years
    Education: BS Computer Science
    """,

    """
    Looking for a Machine Learning Engineer.
    Skills: Python, TensorFlow, PyTorch, AWS
    Experience: 3+ Years
    Education: BS AI
    """,

    """
    Data Analyst Required.
    Skills: SQL, Excel, Power BI
    Experience: Fresh to 1 Year
    Education: BS Data Science
    """
]


def analyze(job):
    return chain.invoke({"job": job})


with ThreadPoolExecutor() as executor:
    results = list(executor.map(analyze, jobs))

for i, result in enumerate(results, start=1):
    print("=" * 70)
    print(f"JOB {i}")
    print("=" * 70)
    print(result)