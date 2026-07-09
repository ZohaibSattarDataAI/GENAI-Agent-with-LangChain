# 📝 AI Grammar Corrector using LangChain & Ollama

A production-ready **AI-powered Grammar Correction Assistant** built with **LangChain**, **Ollama**, **Prompt Engineering**, and **Large Language Models (LLMs)**.

This project enables users to automatically correct grammar, spelling, punctuation, and sentence structure while preserving the original meaning of the text. Instead of manually proofreading sentences, users simply enter their text and receive a professionally corrected version within seconds.

It demonstrates how **LangChain**, **Prompt Templates**, **Runnable Chains**, **Output Parsers**, and **Local LLMs** work together to build intelligent AI-powered writing assistants.

---

# 🚀 Overview

Writing grammatically correct and professional English is essential for emails, reports, assignments, resumes, and everyday communication. However, manually proofreading text can be time-consuming and error-prone.

This project solves that problem using **Large Language Models (LLMs)** powered by LangChain and Ollama.

The application accepts user input, formats it using a prompt template, sends it to a local LLM, and returns a grammatically correct version while preserving the original meaning.

The complete AI workflow is shown below:

```
             User Input
                  │
                  ▼
          Prompt Template
                  │
                  ▼
          ChatOllama (LLM)
                  │
                  ▼
         StrOutputParser
                  │
                  ▼
       Corrected Sentence
```

This project is an excellent beginner-friendly implementation of **Prompt Engineering** and **LangChain Expression Language (LCEL)**.

---

# ✨ Features

- 📝 Grammar Correction
- ✍️ Spelling Correction
- 📚 Punctuation Correction
- 💡 Sentence Structure Improvement
- 🎯 Preserves Original Meaning
- ⚡ Built using LangChain LCEL
- 🤖 Powered by Ollama Local LLM
- 🔒 Completely Offline Execution
- 🚀 Fast AI Responses
- 💬 Interactive Command-Line Interface (CLI)
- 📦 Lightweight and Beginner Friendly
- 🧠 Prompt Engineering Demonstration

---

# 📂 Project Structure

```
AI-Grammar-Corrector/
│
├── grammar_corrector.py
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

### LLM

- Qwen2.5:1.5B

### Prompt Engineering

- PromptTemplate

### Output Parsing

- StrOutputParser

### Programming Language

- Python 3.10+

---

# 🔄 AI Workflow

The application follows a simple LangChain pipeline.

```
User Input
      │
      ▼
PromptTemplate
      │
      ▼
ChatOllama
      │
      ▼
StrOutputParser
      │
      ▼
Corrected Output
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

Download Ollama from

https://ollama.com/download

---

## 5 Pull Required Model

```bash
ollama pull qwen2.5:1.5b
```

---

## 6 Start Ollama

```bash
ollama serve
```

---

## 7 Run the Project

```bash
python grammar_corrector.py
```

---

# 💻 Example

Input

```
i am studing artificial intelligence and i want become ai engineer.
```

---

Output

```
I am studying Artificial Intelligence, and I want to become an AI engineer.
```

---

Another Example

Input

```
he dont likes playing football because it make him tired.
```

Output

```
He doesn't like playing football because it makes him tired.
```

---

# 🧠 Concepts Covered

- LangChain
- Prompt Engineering
- PromptTemplate
- ChatOllama
- Local Large Language Models
- Output Parsers
- Runnable Chains
- LangChain Expression Language (LCEL)
- AI Text Processing
- Grammar Correction

---

# 📈 Future Improvements

Planned features include:

- 🌍 Multi-language Grammar Correction
- 🎙️ Voice-to-Text Grammar Correction
- 🌐 Streamlit Web Interface
- 📱 Flutter Mobile Application
- ⚡ FastAPI Backend
- 📄 Grammar Correction for PDF Files
- 📑 DOCX File Support
- 📋 Copy to Clipboard
- 🧠 AI Writing Assistant
- ✨ Tone Improvement
- 📚 Vocabulary Enhancement
- 🎯 Writing Style Suggestions
- ☁️ Cloud Deployment

---

# 🤖 Recommended Ollama Models

For better performance, consider using the following models.

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best balance of speed and quality |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Excellent grammar correction |
| gemma3:4b | ⭐⭐⭐⭐⭐ Natural language understanding |
| mistral:7b | ⭐⭐⭐⭐⭐ High-quality writing assistance |

---

## Fast Models

- qwen2.5:1.5b ⭐ Recommended
- llama3.2:1b
- gemma3:1b

Best for:

- 8 GB RAM
- Beginners
- Fast responses
- Learning LangChain

---

## Medium Models

- qwen2.5:3b ⭐ Recommended
- llama3.2:3b
- gemma3:4b
- phi4-mini

Best for:

- Better writing quality
- Longer text correction
- Production prototypes

---

## High-End Models

- qwen3:8b
- llama3.1:8b
- mistral-small:24b
- deepseek-r1:8b
- deepseek-r1:14b

Best for:

- Professional writing
- Long documents
- Enterprise AI assistants
- Advanced reasoning

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

By completing this project, you will learn:

- LangChain Fundamentals
- Prompt Engineering
- PromptTemplate
- ChatOllama Integration
- Local LLM Deployment
- Runnable Chains
- Output Parsing
- LangChain Expression Language (LCEL)
- AI-powered Text Processing

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Improving prompt quality
- Supporting additional languages
- Adding new LLMs
- Streamlit Interface
- FastAPI Backend
- Flutter Mobile App
- Writing Assistant Features
- Tone Detection
- Grammar Highlighting
- File Upload Support

---

## 🙌 Author

**Zohaib Sattar**

📧 Email: zabizubi86@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/zohaib-sattar

---

## ⭐ Support & Share the Project

If you found this project useful, consider:

- ⭐ Star this repository
- 🍴 Fork the repository
- 🛠️ Contribute improvements
- 📢 Share it with the AI community

Your support helps grow open-source AI projects and encourages future development.

---

# 📜 License

This project is open-source and available under the **MIT License**.
