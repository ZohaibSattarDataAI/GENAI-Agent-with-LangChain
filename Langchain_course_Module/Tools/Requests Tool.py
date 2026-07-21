from langchain_community.tools import RequestsGetTool
from langchain_community.utilities.requests import TextRequestsWrapper

# Create a requests wrapper
requests_wrapper = TextRequestsWrapper()

# Enable dangerous requests explicitly
tool = RequestsGetTool(
    requests_wrapper=requests_wrapper,
    allow_dangerous_requests=True
)

result = tool.invoke("https://github.com/ZohaibSattarDataAI")

print(result)