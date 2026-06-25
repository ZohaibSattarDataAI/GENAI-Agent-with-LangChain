from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.2",
    task="text-generation",
    huggingfacehub_api_token='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',
    temperature=0.7,
    # max_new_tokens=150
)

chat = ChatHuggingFace(llm=llm)

result = chat.invoke(
    "write skills which is needed for AI engineering"
)
print(result.content)