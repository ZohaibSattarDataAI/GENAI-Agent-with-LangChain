# 📧 AI Email Generator using LangChain & Ollama

A production-ready **AI-powered Email Generator** built with **LangChain**, **Ollama**, and **Large Language Models (LLMs)**.

This project automatically generates **professional, personalized, and well-structured emails** for various real-world scenarios, including leave applications, internship requests, job applications, meeting requests, thank-you emails, complaint emails, apology emails, project updates, and custom emails.

It demonstrates how **LangChain Runnables**, **Prompt Engineering**, and **LLMs** can be combined to automate business and personal email writing.

---

# 🚀 Overview

Writing professional emails takes time and requires proper structure, tone, and grammar.

This AI Email Generator simplifies the process by allowing users to provide a few details, while the AI generates a complete email within seconds.

The project uses **LangChain Runnable Chains** to create a clean and modular AI workflow:

```
User Input
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
Generated Email
```

This project is an excellent beginner-to-intermediate example of **LangChain Runnables** and **Prompt Engineering**.

---

# ✨ Features

- 📧 AI-generated professional emails
- 🧠 Prompt Engineering with LangChain
- ⚡ Runnable Chains
- 🤖 Local LLM support via Ollama
- 📝 Multiple email templates
- 💼 Business & personal email generation
- 🎯 Context-aware email creation
- 📄 Automatic subject generation
- ✨ Clean and readable email formatting
- 🔒 Runs completely offline (with Ollama)
- 🖥️ Simple command-line interface (CLI)
- 🚀 Beginner-friendly project structure

---

# 📂 Supported Email Types

The generator currently supports the following email templates:

- Leave Application
- Internship Request
- Job Application
- Meeting Request
- Project Update
- Thank You Email
- Complaint Email
- Apology Email
- Custom Email

---

# 🏗️ Project Structure

```
Email Generator/
│
├── email_generator.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

# ⚙️ Tech Stack

### AI Framework

- LangChain

### LLM

- Ollama

### Programming Language

- Python 3.10+

### Output Parsing

- StrOutputParser

### Prompt Engineering

- ChatPromptTemplate

---

# 🔄 LangChain Workflow

This project uses the Runnable Pipeline:

```python
Prompt
   │
   ▼
ChatOllama
   │
   ▼
StrOutputParser
```

Pipeline:

```python
chain = prompt | model | parser
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

Download and install Ollama:

https://ollama.com/download

---

## 5 Pull an AI Model

Example:

```bash
ollama pull qwen2.5:3b
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
python email_generator.py
```

---

# 💻 Example

```
==========================================================
AI EMAIL GENERATOR
==========================================================

1. Leave Application
2. Internship Request
3. Job Application
4. Meeting Request
5. Project Update
6. Thank You Email
7. Complaint Email
8. Apology Email
9. Custom Email

0. Exit
```

---

Example Input

```
Receiver Name:
Team Lead

Sender:
Zohaib Sattar

Purpose:
Request for 2 days leave

Additional Details:
I need leave to attend my close friend's wedding ceremony.
```

---

Example Output

```
Subject: Request for Two Days Leave

Dear Team Lead,

I hope you are doing well.

I am writing to request two days of leave to attend my close friend's wedding ceremony. I will ensure that all my pending tasks are completed before my leave.

I kindly request you to approve my leave request.

Thank you for your consideration.

Best regards,

Zohaib Sattar
```

---

# 🧠 Concepts Covered

- LangChain
- Runnable Chains
- Prompt Engineering
- ChatPromptTemplate
- StrOutputParser
- Chat Models
- LLM Integration
- Ollama
- CLI Applications
- AI Workflow Design

---

# 📈 Future Improvements

Planned features include:

- Streamlit GUI
- FastAPI Integration
- Email Export as PDF
- Save Email as TXT
- Email History
- Copy to Clipboard
- Streaming Responses
- Multi-language Support
- Grammar Correction
- Email Rewriting
- Tone Selection
- Email Length Selection
- Follow-up Email Generator
- Email Summarizer
- Email Translator

---

# 🤖 Recommended Ollama Models

For better performance, you can use any of the following models.

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best balance of speed and quality |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Professional emails |
| gemma3:4b | ⭐⭐⭐⭐⭐ Natural writing |
| mistral:7b | ⭐⭐⭐⭐⭐ High-quality business emails |

---

## Fast Models

- qwen2.5:1.5b
- llama3.2:1b
- gemma3:1b

Best for:

- Low RAM PCs
- Fast inference
- Learning LangChain

---

## Medium Models

- qwen2.5:3b ⭐ Recommended
- llama3.2:3b ⭐ Recommended
- gemma3:4b
- phi4-mini
- granite3.3

Best for:

- Daily development
- Professional email generation
- Better prompt following

---

## High-End Models

- qwen3:8b
- llama3.1:8b
- llama3.3:70b
- mistral-small:24b
- mixtral:8x7b
- deepseek-r1:8b
- deepseek-r1:14b

Best for:

- Production applications
- Enterprise AI
- Long-form writing
- Highly accurate responses

---

# 💻 Minimum System Requirements

## For 1B–3B Models

- RAM: 8 GB+
- CPU: Intel i5 / Ryzen 5
- GPU: Optional

---

## For 7B–8B Models

- RAM: 16 GB+
- GPU: Recommended

---

## For 14B+ Models

- RAM: 32 GB+
- Dedicated GPU Recommended

---

# 📚 Learning Outcomes

By exploring this project, you will learn:

- LangChain Runnables
- Prompt Engineering
- LLM Integration
- Ollama
- Output Parsers
- AI Application Development
- Python Project Structure
- Business Email Automation

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Adding new email templates
- Improving prompts
- Optimizing AI responses
- Fixing bugs
- Improving documentation
- Adding Streamlit UI
- FastAPI integration
- Multi-language support

---

# 👨‍💻 Author

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

Your support helps grow open-source AI projects and encourages future development.

---


