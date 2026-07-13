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
You are a professional ATS Resume Reviewer and Senior HR Recruiter.

Analyze the following resume.

Return the response using EXACTLY the following Markdown format.

# Resume Analysis Report

## 1. Candidate Summary
(Write 3-4 lines)

## 2. Overall Resume Score
Give score out of 10.

## 3. Technical Skills
- Skill 1
- Skill 2
- Skill 3

## 4. Soft Skills
- Skill 1
- Skill 2

## 5. Education
- Degree
- University
- CGPA (if available)

## 6. Work Experience
List all experience.

## 7. Projects
List projects.

## 8. Certifications
List certifications.

## 9. Strengths
List strengths.

## 10. Weaknesses
List weaknesses.

## 11. Missing Skills
Mention important missing skills.

## 12. ATS Improvement Suggestions
Give at least 5 suggestions.

## 13. Suitable Job Roles
Recommend 5 job roles.

## 14. Final Verdict

Excellent / Very Good / Good / Needs Improvement

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