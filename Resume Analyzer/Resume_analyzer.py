from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ---------------------------------------
# Load Resume PDF
# ---------------------------------------

loader = PyPDFLoader(
    r"C:\Users\ZohaibSattar_Data_AI\Downloads\ZohaibSattar_Data_AI .pdf"
)

documents = loader.load()

print(f"Total Pages: {len(documents)}")

# Merge all pages

resume_text = "\n\n".join(doc.page_content for doc in documents)

# ---------------------------------------
# Load Local LLM
# ---------------------------------------

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# ---------------------------------------
# Prompt
# ---------------------------------------

prompt = ChatPromptTemplate.from_template("""
You are an expert HR Recruiter and Resume Reviewer.

Carefully analyze the resume below.

Generate a professional report using the following format.

# Resume Analysis Report

## Candidate Summary
Write a short professional summary.

---

## Overall Resume Score
Score the resume out of 10.

---

## Technical Skills
List all technical skills.

---

## Soft Skills
List all soft skills.

---

## Education
Extract education details.

---

## Work Experience
Extract work experience.

---

## Projects
List projects mentioned.

---

## Certifications
List certifications.

---

## Strengths
Mention major strengths.

---

## Weaknesses
Mention weaknesses.

---

## Missing Skills
Mention missing skills if any.

---

## ATS Optimization Tips
Suggest ATS improvements.

---

## Resume Improvement Suggestions
Give practical suggestions.

---

## Suitable Job Roles
Suggest suitable job positions.

---

## Final Recommendation

One of:

Excellent

Very Good

Good

Needs Improvement

Resume:

{resume}

""")

# ---------------------------------------
# Output Parser
# ---------------------------------------

parser = StrOutputParser()

# ---------------------------------------
# Chain
# ---------------------------------------

chain = prompt | model | parser

# ---------------------------------------
# Analyze Resume
# ---------------------------------------

result = chain.invoke({
    "resume": resume_text
})

# ---------------------------------------
# Print Report
# ---------------------------------------

print("\n")
print("=" * 80)
print(result)
print("=" * 80)