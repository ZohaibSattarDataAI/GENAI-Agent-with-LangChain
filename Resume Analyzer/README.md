# 📄 AI Resume Analyzer using LangChain & Ollama

A production-ready **AI-powered Resume Analyzer** built with **LangChain**, **Ollama**, and **Large Language Models (LLMs)**.

This project enables users to upload a **resume (PDF)** and receive an AI-generated analysis, including skills, strengths, weaknesses, career summary, technical expertise, and improvement suggestions. It leverages **LangChain Runnables**, **Prompt Engineering**, and **Local LLMs** to automate resume evaluation while running completely offline.

Whether you're a student, job seeker, recruiter, HR professional, or developer, this project demonstrates how modern AI can intelligently analyze resumes and provide meaningful insights.

---

#  Overview

Reviewing resumes manually can be time-consuming and inconsistent. This AI Resume Analyzer simplifies the process by extracting information from a PDF resume and generating structured insights within seconds.

The application uses **LangChain Runnable Chains** to build a modular AI workflow that processes resume content and produces an intelligent analysis.

Workflow:

```
Resume PDF
     │
     ▼
PyPDFLoader
     │
     ▼
Extract Resume Text
     │
     ▼
Prompt Template
     │
     ▼
Large Language Model (Ollama)
     │
     ▼
Output Parser
     │
     ▼
Resume Analysis
```

This project is an excellent practical example of **Prompt Engineering**, **LangChain Runnables**, and **LLM-powered Resume Analysis**.

---

# ✨ Features

- 📄 Resume PDF analysis
- 🤖 AI-powered resume evaluation
- 🧠 Prompt Engineering with LangChain
- ⚡ Runnable Chains
- 🏠 Local LLM support using Ollama
- 🎯 Skill extraction
- 💼 Experience analysis
- 🎓 Education summary
- 📊 Strengths identification
- ⚠️ Weakness detection
- 💡 Resume improvement suggestions
- 📈 Career recommendations
- 🖥️ Command-line interface (CLI)
- 🔒 Completely offline execution
- 🚀 Lightweight and beginner-friendly

---

# 📂 Project Structure

```
Resume-Analyzer-using-LangChain/
│
├── resume_analyzer.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

# ⚙️ Tech Stack

### AI Framework

- LangChain

### Large Language Models

- Ollama

### Programming Language

- Python 3.10+

### Document Loader

- PyPDFLoader

### Output Parsing

- StrOutputParser

### Prompt Engineering

- ChatPromptTemplate

---

# 🔄 LangChain Workflow

```
Resume PDF
     │
     ▼
PyPDFLoader
     │
     ▼
Extract Resume Text
     │
     ▼
ChatPromptTemplate
     │
     ▼
ChatOllama
     │
     ▼
StrOutputParser
     │
     ▼
Resume Analysis
```

Pipeline:

```python
chain = prompt | model | parser
```

---

# 🧠 Flowchart

```
                ┌────────────────────┐
                │    Resume PDF      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   PyPDFLoader      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Extract Resume Text│
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Prompt Template    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ ChatOllama (LLM)   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ StrOutputParser    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Resume Analysis    │
                └────────────────────┘
```

---

# 🛠️ Installation

## 1 Clone Repository

```bash
git clone https://github.com/ZohaibSattarDataAI/GENAI-Agent-with-LangChain.git

cd GENAI-Agent-with-LangChain
```

---

## 2 Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Install Ollama

Download Ollama from:

https://ollama.com/download

---

## 5 Pull an AI Model

```bash
ollama pull qwen2.5:1.5b
```

or

```bash
ollama pull llama3.2:3b
```

---

## 6 Start Ollama

```bash
ollama serve
```

---

## 7 Run the Project

```bash
python resume_analyzer.py
```

---

# 💻 Example

```
Resume Analysis

Name:
John Doe

Overall Score:
8.9 / 10

Skills:
- Python
- Machine Learning
- SQL
- Power BI
- LangChain

Strengths:
- Strong AI background
- Multiple technical projects
- Good programming knowledge

Weaknesses:
- Limited industry experience
- Few certifications

Suggestions:
- Add measurable project achievements
- Include GitHub portfolio
- Improve ATS keywords
```

---

# 🧠 Concepts Covered

- LangChain
- Runnable Chains
- Prompt Engineering
- ChatPromptTemplate
- StrOutputParser
- PyPDFLoader
- Resume Analysis
- Large Language Models
- Ollama
- AI-powered Document Analysis

---

# 📈 Future Improvements

Planned features include:

- Resume ATS Score
- Keyword Matching
- Job Description Comparison
- Resume Ranking
- Skill Gap Analysis
- Interview Question Generation
- Cover Letter Generator
- Streamlit GUI
- FastAPI Integration
- PDF Report Export
- DOCX Report Export
- Resume Rewriting
- Multi-language Support
- Chroma Vector Database
- RAG-based Resume Analysis

---

# 🤖 Recommended Ollama Models

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best overall resume analysis |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Accurate resume evaluation |
| gemma3:4b | ⭐⭐⭐⭐⭐ Professional analysis |
| mistral:7b | ⭐⭐⭐⭐⭐ Advanced reasoning |

---

## Fast Models

- qwen2.5:1.5b ⭐ Recommended
- llama3.2:1b
- gemma3:1b

Best for:

- 8 GB RAM
- Fast responses
- Learning LangChain

---

## Medium Models

- qwen2.5:3b ⭐ Recommended
- llama3.2:3b ⭐ Recommended
- gemma3:4b
- phi4-mini
- granite3.3

---

## High-End Models

- qwen3:8b
- llama3.1:8b
- llama3.3:70b
- mixtral:8x7b
- mistral-small:24b
- deepseek-r1:14b

---

# 🎯 Resume Analysis Capabilities

The analyzer can identify:

- Contact Information
- Professional Summary
- Technical Skills
- Soft Skills
- Education
- Certifications
- Work Experience
- Projects
- Strengths
- Weaknesses
- ATS Optimization Tips
- Career Suggestions

---

# 💻 Minimum System Requirements

## Small Models (1B–3B)

- RAM: 8 GB+
- CPU: Intel i5 / Ryzen 5
- GPU: Optional

---

## Medium Models (7B–8B)

- RAM: 16 GB+
- GPU Recommended

---

## Large Models (14B+)

- RAM: 32 GB+
- Dedicated GPU Recommended

---

# 📚 Learning Outcomes

By exploring this project, you will learn:

- LangChain Runnables
- Prompt Engineering
- Resume Analysis using AI
- Document Processing
- PyPDFLoader
- ChatOllama
- Local LLM Integration
- AI Workflow Design
- Python AI Applications

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Improving prompts
- ATS scoring
- Resume ranking
- RAG integration
- Chroma Vector Database
- Streamlit UI
- FastAPI backend
- Multi-PDF support
- Dashboard development

---

## 🙌 Author



**Zohaib Sattar**  
📧 Email: [zabizubi86@gmail.com](mailto:zabizubi86@gmail.com)  
🔗 LinkedIn: [Zohaib Sattar](https://www.linkedin.com/in/zohaib-sattar)  


---

## ⭐ Support & Share the Project

If you found this project useful, consider:

- ⭐ Star this repository
- 🍴 Fork the repository
- 🛠️ Contribute improvements
- 📢 Share it with the AI community

---

# 📜 License

This project is open-source and available under the **MIT License**.
