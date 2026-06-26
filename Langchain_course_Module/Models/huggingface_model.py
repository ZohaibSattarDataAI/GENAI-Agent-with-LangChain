from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.2",
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0,
    # max_new_tokens=150
)

chat = ChatHuggingFace(llm=llm)

result = chat.invoke(

"""Act as a Principal AI Engineer at a top AI company.

Create the ultimate AI Engineer roadmap for 2026.

Include:

* Programming Skills
* Mathematics
* Machine Learning
* Deep Learning
* LLM Engineering
* RAG Systems
* Agentic AI
* LangChain
* LangGraph
* MCP (Model Context Protocol)
* Fine-Tuning
* AI Evaluation
* Vector Databases
* AI Deployment
* FastAPI
* Docker
* Kubernetes
* Cloud Platforms
* MLOps
* AI System Design

For each skill provide:

* Learning resources
* Projects
* Interview questions
* Industry use cases
* Estimated learning time

Finally create a job-ready roadmap from Beginner to AI Engineer.
"""
)
print(result.content)