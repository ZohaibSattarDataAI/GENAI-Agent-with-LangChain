from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ==========================
# LLM
# ==========================
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.7
)

parser = StrOutputParser()

# ==========================
# Chain 1 : Generate Outline
# ==========================
outline_prompt = PromptTemplate(
    template="""
You are a professional blog writer.

Create a detailed blog outline for the topic:

Topic:
{topic}

The outline should include:
- Introduction
- 4 to 6 main headings
- Conclusion
""",
    input_variables=["topic"]
)

outline_chain = outline_prompt | model | parser

# ==========================
# Chain 2 : Write Blog
# ==========================
blog_prompt = PromptTemplate(
    template="""
Write a professional blog based on the following outline.

Outline:
{outline}

Requirements:
- Around 700 words
- Easy English
- Use headings
- Include examples
- Add a conclusion
""",
    input_variables=["outline"]
)

blog_chain = blog_prompt | model | parser

# ==========================
# Chain 3 : Generate SEO Title
# ==========================
title_prompt = PromptTemplate(
    template="""
Generate one catchy SEO-friendly title for the following blog.

Blog:
{blog}

Return only the title.
""",
    input_variables=["blog"]
)

title_chain = title_prompt | model | parser

# ==========================
# User Input
# ==========================
topic = input("Enter Blog Topic: ")

# Step 1
outline = outline_chain.invoke({
    "topic": topic
})

# Step 2
blog = blog_chain.invoke({
    "outline": outline
})

# Step 3
title = title_chain.invoke({
    "blog": blog
})

# ==========================
# Output
# ==========================
print("\n" + "="*60)
print("SEO TITLE")
print("="*60)
print(title)

print("\n" + "="*60)
print("BLOG")
print("="*60)
print(blog)