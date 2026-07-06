# 📄 Chat with PDF using LangChain, Ollama & RAG

A production-ready **AI-powered PDF Question Answering Assistant** built with **LangChain**, **Ollama**, **Retrieval-Augmented Generation (RAG)**, **Vector Databases**, and **Large Language Models (LLMs)**.

This project enables users to upload PDF documents and interact with them using natural language. Instead of manually searching through lengthy documents, users can simply ask questions and receive accurate, context-aware answers generated directly from the PDF content.

It demonstrates how **LangChain**, **RAG Pipelines**, **Vector Embeddings**, **Document Loaders**, and **Local LLMs** work together to build intelligent document-based AI assistants.

---

# 🚀 Overview

Large Language Models cannot accurately answer questions about private documents unless the document content is provided as context.

This project solves that problem using **Retrieval-Augmented Generation (RAG)**.

The workflow extracts text from uploaded PDFs, splits it into smaller chunks, converts each chunk into vector embeddings, stores them inside a vector database, retrieves the most relevant chunks for every user query, and finally generates accurate answers using a local LLM.

The complete AI workflow is shown below:

```
                PDF File
                    │
                    ▼
          PDF Document Loader
                    │
                    ▼
           Text Splitter
                    │
                    ▼
          Vector Embeddings
                    │
                    ▼
      FAISS / Chroma Vector Store
                    │
                    ▼
      Semantic Similarity Search
                    │
                    ▼
         Relevant Document Chunks
                    │
                    ▼
             Ollama LLM
                    │
                    ▼
          AI Generated Answer
```

This project is an excellent real-world implementation of **Retrieval-Augmented Generation (RAG)** using LangChain.

---

# ✨ Features

- 📄 Upload PDF documents
- 🤖 Chat with your documents
- 📚 Retrieval-Augmented Generation (RAG)
- 🧠 Context-aware question answering
- 🔍 Semantic document search
- ⚡ LangChain Runnable Chains
- 📦 Local LLM support with Ollama
- 🔒 Completely offline execution
- 📑 Automatic document chunking
- 🚀 Fast vector similarity search
- 📝 Multiple question support
- 💬 Conversational document interaction
- 🖥️ Simple command-line interface (CLI)
- 🎯 Beginner-friendly architecture

---

# 📂 Project Structure

```
Chat-with-PDF-using-LangChain/
│
├── pdf_chat.py
├── README.md
├── requirements.txt
├── sample_pdfs/
└── screenshots/
```

---

# ⚙️ Tech Stack

### AI Framework

- LangChain

### Large Language Models

- Ollama

### Embedding Models

- Nomic Embed Text
- BGE Embeddings
- Sentence Transformers

### Vector Databases

- FAISS
- Chroma

### Document Processing

- PyPDFLoader
- RecursiveCharacterTextSplitter

### Programming Language

- Python 3.10+

---

# 🔄 AI Workflow

This project follows a complete Retrieval-Augmented Generation pipeline.

```
PDF
 │
 ▼
Document Loader
 │
 ▼
Text Splitter
 │
 ▼
Embeddings
 │
 ▼
Vector Database
 │
 ▼
Retriever
 │
 ▼
Prompt
 │
 ▼
LLM
 │
 ▼
Answer
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

## 5 Pull Required Models

LLM

```bash
ollama pull qwen2.5:3b
```

Embeddings

```bash
ollama pull nomic-embed-text
```

---

## 6 Start Ollama

```bash
ollama serve
```

---

## 7 Run the Project

```bash
python pdf_chat.py
```

---

# 💻 Example

Upload PDF

```
Resume.pdf
```

---

Ask Questions

```
What is the candidate's educational background?

Summarize the document.

What programming languages are mentioned?

What projects are included?

Explain the experience section.
```

---

Example Output

```
Question:

What machine learning algorithms are discussed?

Answer:

The document discusses several supervised learning algorithms including
Linear Regression, Logistic Regression, Decision Trees, Random Forest,
Support Vector Machines, and XGBoost. It also explains their advantages,
limitations, and practical applications.
```

---

# 🧠 Concepts Covered

- LangChain
- Retrieval-Augmented Generation (RAG)
- Document Loaders
- Recursive Text Splitting
- Embeddings
- Vector Databases
- Semantic Search
- Similarity Search
- Prompt Engineering
- Runnable Chains
- Local LLMs
- Context Retrieval
- Question Answering

---

# 📈 Future Improvements

Planned features include:

- Streamlit Interface
- FastAPI Backend
- Multiple PDF Support
- Chat History
- Memory Integration
- Source Citation
- Highlight Relevant Paragraphs
- PDF Summarization
- Multi-language Support
- Voice-based Question Answering
- OCR Support
- DOCX Support
- PowerPoint Support
- Image-based PDF Support
- Web Deployment

---

# 🤖 Recommended Ollama Models

For better performance, consider using the following models.

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best balance of speed and quality |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Excellent reasoning |
| gemma3:4b | ⭐⭐⭐⭐⭐ Natural responses |
| mistral:7b | ⭐⭐⭐⭐⭐ High-quality document understanding |

---

## Fast Models

- qwen2.5:1.5b
- llama3.2:1b
- gemma3:1b

Best for:

- 8 GB RAM
- Learning LangChain
- Fast inference

---

## Medium Models

- qwen2.5:3b ⭐ Recommended
- llama3.2:3b ⭐ Recommended
- gemma3:4b
- phi4-mini
- granite3.3

Best for:

- RAG systems
- Production prototypes
- Better context understanding

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

- Enterprise AI
- Long documents
- Advanced reasoning
- Research assistants

---

# 🤖 Recommended Embedding Models

| Embedding Model | Quality |
|-----------------|----------|
| nomic-embed-text | ⭐⭐⭐⭐⭐ Recommended |
| bge-large | ⭐⭐⭐⭐⭐ |
| bge-base | ⭐⭐⭐⭐ |
| all-MiniLM-L6-v2 | ⭐⭐⭐⭐ |
| mxbai-embed-large | ⭐⭐⭐⭐⭐ |

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

- LangChain
- Retrieval-Augmented Generation (RAG)
- Document Question Answering
- Embedding Models
- Vector Databases
- Semantic Search
- Prompt Engineering
- Runnable Chains
- Local LLM Deployment
- AI Document Assistants

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Adding new embedding models
- Improving prompts
- Optimizing retrieval quality
- Supporting additional document formats
- Streamlit UI
- FastAPI integration
- Better chunking strategies
- Hybrid Search
- OCR Support
- Multi-document conversations

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

# 📜 License

This project is open-source and available under the **MIT License**.
