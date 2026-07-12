# 📄 PDF Question Answering Chatbot using LangChain & Ollama

A production-ready **AI-powered PDF Question Answering (QA) Chatbot** built with **LangChain**, **Ollama**, and **Large Language Models (LLMs)**.

This project enables users to ask **natural language questions** about the contents of a PDF document. The chatbot reads the PDF, understands its content using a Large Language Model, and generates accurate answers based solely on the uploaded document.

Whether you're working with resumes, research papers, reports, notes, ebooks, or documentation, this project demonstrates how modern AI can transform static PDFs into interactive, intelligent assistants.

---

# 🚀 Overview

Searching through lengthy PDF documents manually can be slow and inefficient. This AI-powered chatbot simplifies the process by allowing users to ask questions in plain English and receive instant answers extracted from the document.

The application uses **LangChain Runnable Chains**, **Prompt Engineering**, and a **local Ollama LLM** to build a lightweight and completely offline PDF Question Answering system.

Workflow:

```
PDF Document
      │
      ▼
PyPDFLoader
      │
      ▼
Extract Text
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
Answer to User
```

This project is an excellent practical example of **Prompt Engineering**, **LangChain Runnables**, and **LLM-powered Document Question Answering**.

---

# ✨ Features

- 📄 Read PDF documents
- 🤖 AI-powered Question Answering
- 🧠 Prompt Engineering with LangChain
- ⚡ Runnable Chains
- 🏠 Local LLM support using Ollama
- 💬 Interactive chatbot interface (CLI)
- 📖 Works with resumes, reports, books, and research papers
- 📌 Context-aware responses
- 🔒 Completely offline execution
- 🖥️ Beginner-friendly implementation
- 🚀 Fast and lightweight architecture

---

# 📂 Project Structure

```
PDF-Question-Answering-using-LangChain/
│
├── pdf_chatbot.py
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

This project uses a simple Runnable pipeline.

```
PDF
 │
 ▼
PyPDFLoader
 │
 ▼
Extract Text
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
Answer
```

Pipeline:

```python
chain = prompt | model | parser
```

---

# 🧠 Flowchart

```
                 ┌────────────────────┐
                 │   PDF Document     │
                 └─────────┬──────────┘
                           │
                           ▼
                ┌────────────────────┐
                │   PyPDFLoader      │
                └─────────┬──────────┘
                          │
                          ▼
               ┌─────────────────────┐
               │ Extract PDF Content │
               └─────────┬───────────┘
                         │
                         ▼
               ┌─────────────────────┐
               │ User asks Question  │
               └─────────┬───────────┘
                         │
                         ▼
               ┌─────────────────────┐
               │ Prompt Template     │
               └─────────┬───────────┘
                         │
                         ▼
               ┌─────────────────────┐
               │ ChatOllama (LLM)    │
               └─────────┬───────────┘
                         │
                         ▼
               ┌─────────────────────┐
               │ StrOutputParser     │
               └─────────┬───────────┘
                         │
                         ▼
               ┌─────────────────────┐
               │ Final Answer        │
               └─────────────────────┘
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

Example:

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
python pdf_chatbot.py
```

---

# 💻 Example

```
Ask a question:

What skills are mentioned in the resume?
```

Example Output

```
The resume mentions skills including Python, Machine Learning,
Deep Learning, SQL, Power BI, LangChain, and Artificial Intelligence.
```

---

Another Example

```
Ask a question:

Which university is mentioned?
```

Output

```
The document mentions
The Islamia University of Bahawalpur.
```

---

Another Example

```
Ask a question:

What is the CGPA?
```

Output

```
The document states that the CGPA is 3.5.
```

---

# 🧠 Concepts Covered

- LangChain
- Runnable Chains
- Prompt Engineering
- ChatPromptTemplate
- StrOutputParser
- ChatOllama
- PyPDFLoader
- PDF Processing
- Document Question Answering
- Large Language Models
- Offline AI Applications

---

# 📈 Future Improvements

Planned features include:

- RecursiveCharacterTextSplitter
- Ollama Embeddings
- Chroma Vector Database
- FAISS Integration
- Retrieval-Augmented Generation (RAG)
- Streamlit GUI
- FastAPI Backend
- Multiple PDF Support
- Chat History
- Memory Integration
- Source Citation
- Multi-language Support
- OCR for Scanned PDFs
- Web Interface
- Voice Question Answering

---

# 🤖 Recommended Ollama Models

For better document understanding, use one of the following models.

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best overall PDF understanding |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Accurate question answering |
| gemma3:4b | ⭐⭐⭐⭐⭐ Natural language reasoning |
| mistral:7b | ⭐⭐⭐⭐⭐ Large document analysis |

---

## Fast Models

- qwen2.5:1.5b ⭐ Recommended
- llama3.2:1b
- gemma3:1b

Best for:

- 8 GB RAM
- Fast inference
- Learning LangChain
- Small PDF documents

---

## Medium Models

- qwen2.5:3b ⭐ Recommended
- llama3.2:3b ⭐ Recommended
- gemma3:4b
- phi4-mini
- granite3.3

Best for:

- Research papers
- Technical documentation
- Resume analysis
- Daily AI applications

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

- Enterprise document analysis
- Large reports
- Multi-document QA
- Research projects

---

# 🎯 Applications

This chatbot can answer questions from:

- 📄 Resume/CV
- 📚 Research Papers
- 📖 Books
- 📑 Reports
- 📰 Articles
- 📋 Notes
- 📘 Documentation
- 📜 Contracts
- 📊 Business Reports
- 🎓 Educational Material
- 📁 Company Documents
- 📄 Any Text-based PDF

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
- PDF Processing
- Document Question Answering
- ChatOllama
- Local LLM Integration
- PyPDFLoader
- AI Workflow Design
- Offline AI Applications
- Python Automation

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Adding RAG support
- Implementing Chroma Vector Database
- FAISS Integration
- Streamlit UI
- FastAPI Backend
- Memory Support
- Multi-PDF Chat
- OCR Integration
- Chat History
- Performance Optimization

---

## 🙌 Author

**Zohaib Sattar**

📧 Email: zabizubi86@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/zohaib-sattar-5680ab2a5/

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
