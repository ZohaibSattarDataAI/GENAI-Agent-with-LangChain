
# 📄 YouTube Video Chatbot using LangChain, Ollama & FAISS

A production-ready **AI-powered YouTube Question Answering Chatbot** built with **LangChain**, **Ollama**, **FAISS**, and **Large Language Models (LLMs)**.

This project allows users to **chat with any YouTube video** by automatically extracting the video's transcript, converting it into embeddings, storing it inside a vector database, and answering questions using **Retrieval-Augmented Generation (RAG)**.

Instead of watching an entire video, users can simply ask questions such as:

* *What is this video about?*
* *Summarize the video.*
* *What are the key takeaways?*
* *Explain a specific topic discussed in the video.*

The chatbot answers **only from the video's transcript**, making responses accurate, context-aware, and grounded in the video content.

---

# 🚀 Overview

Long YouTube videos often contain valuable information, but finding specific details can be time-consuming.

This project solves that problem by transforming YouTube videos into an **interactive AI chatbot**.

The application automatically:

* Fetches the YouTube transcript
* Splits it into chunks
* Creates vector embeddings
* Stores them in FAISS
* Retrieves relevant chunks
* Uses a local Ollama LLM to generate accurate answers

Everything runs **locally**, ensuring privacy and eliminating API costs.

---

# ⚡ Workflow

```
YouTube Video
        │
        ▼
Video ID
        │
        ▼
YouTube Transcript API
        │
        ▼
Transcript
        │
        ▼
RecursiveCharacterTextSplitter
        │
        ▼
Ollama Embeddings
        │
        ▼
FAISS Vector Database
        │
        ▼
Retriever
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
Final Answer
```

This project demonstrates a complete **Retrieval-Augmented Generation (RAG)** pipeline using **LangChain** and **Ollama**.

---

# ✨ Features

* 🎥 Chat with any YouTube video
* 📝 Automatic transcript extraction
* 🧠 Retrieval-Augmented Generation (RAG)
* ⚡ LangChain Runnable Chains
* 💬 Interactive command-line chatbot
* 🔍 Semantic search using FAISS
* 📚 Context-aware question answering
* 🤖 Local LLM with Ollama
* 🔒 100% Offline (after transcript retrieval)
* 🚀 Fast and lightweight
* 🖥️ Beginner-friendly implementation

---

# 📂 Project Structure

```
YouTube-Chatbot-LangChain/
│
├── youtube_chatbot.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

# ⚙️ Tech Stack

## AI Framework

* LangChain

## Large Language Model

* Ollama

## Embedding Model

* nomic-embed-text

## Vector Database

* FAISS

## Transcript Loader

* youtube-transcript-api

## Programming Language

* Python 3.10+

## Prompt Engineering

* ChatPromptTemplate

## Output Parsing

* StrOutputParser

---

# 🔄 LangChain RAG Workflow

```
YouTube Video
      │
      ▼
Transcript Loader
      │
      ▼
Document
      │
      ▼
Text Splitter
      │
      ▼
Embeddings
      │
      ▼
FAISS
      │
      ▼
Retriever
      │
      ▼
Prompt
      │
      ▼
ChatOllama
      │
      ▼
Answer
```

Pipeline:

```python
retriever → prompt → ChatOllama → StrOutputParser
```

---

# 🧠 Flowchart

```
              ┌─────────────────────────┐
              │     YouTube Video       │
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ Video Transcript Loader │
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │  Split into Chunks      │
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ Ollama Embeddings       │
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ FAISS Vector Database   │
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ Retrieve Relevant Chunks│
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ ChatPromptTemplate      │
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ ChatOllama              │
              └────────────┬────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ Final AI Answer         │
              └─────────────────────────┘
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

[https://ollama.com/download](https://ollama.com/download)

---

## 5 Pull Required Models

Embedding Model

```bash
ollama pull nomic-embed-text
```

LLM

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
python youtube_chatbot.py
```

---

# 💻 Example

Enter a YouTube Video ID:

```
Gfr50f6ZBvo
```

Ask:

```
What is this video about?
```

Output

```
The video introduces DeepMind, its mission, and recent advances in
Artificial Intelligence research.
```

---

Another Example

```
Summarize the video.
```

Output

```
The speaker explains the fundamentals of AI, discusses DeepMind's
research, and highlights future opportunities in artificial intelligence.
```

---

Another Example

```
What are the key points?
```

Output

```
• Introduction to AI
• DeepMind research
• Machine Learning concepts
• Future applications
• Challenges and opportunities
```

---

# 🧠 Concepts Covered

* LangChain
* Retrieval-Augmented Generation (RAG)
* FAISS Vector Database
* RecursiveCharacterTextSplitter
* Ollama Embeddings
* ChatOllama
* Prompt Engineering
* Semantic Search
* YouTube Transcript Processing
* Document Retrieval
* Local LLM Applications

---

# 📈 Future Improvements

Planned features include:

* 🌐 Streamlit Web App
* ⚡ FastAPI Backend
* 🎥 Multiple YouTube Video Support
* 💾 Persistent FAISS Storage
* 📝 Chat History
* 🧠 Conversation Memory
* 📌 Timestamp References
* 🔗 Source Citation
* 🌍 Multi-language Support
* 🎤 Voice Questions
* 📥 YouTube Playlist Chat
* 📱 Web Interface

---

# 🤖 Recommended Ollama Models

## ⭐ Best Overall

| Model       | Recommended For                |
| ----------- | ------------------------------ |
| qwen2.5:3b  | ⭐⭐⭐⭐⭐ Best overall             |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Accurate answers         |
| gemma3:4b   | ⭐⭐⭐⭐⭐ Reasoning                |
| mistral:7b  | ⭐⭐⭐⭐⭐ Long transcript analysis |

---

## Fast Models

* qwen2.5:1.5b ⭐ Recommended
* llama3.2:1b
* gemma3:1b

Best for:

* 8 GB RAM
* Learning LangChain
* Quick responses
* Small videos

---

## Medium Models

* qwen2.5:3b ⭐
* llama3.2:3b ⭐
* gemma3:4b
* phi4-mini
* granite3.3

Best for:

* Technical videos
* Educational lectures
* Tutorials
* AI content

---

## High-End Models

* qwen3:8b
* llama3.1:8b
* deepseek-r1:8b
* mistral-small:24b
* mixtral:8x7b
* llama3.3:70b

Best for:

* Long-form videos
* Enterprise AI
* Research analysis
* Advanced reasoning

---

# 🎯 Applications

This chatbot can answer questions from:

* 🎥 YouTube Tutorials
* 🎓 Educational Lectures
* 💻 Programming Tutorials
* 🤖 AI & Machine Learning Videos
* 📈 Business Talks
* 🎤 Conference Presentations
* 📚 Online Courses
* 🔬 Research Discussions
* 📺 Tech Reviews
* 🎙️ Podcasts
* 📖 Learning Content
* 🌍 Any YouTube video with available transcripts

---

# 💻 Minimum System Requirements

## Small Models (1B–3B)

* RAM: 8 GB+
* CPU: Intel i5 / Ryzen 5
* GPU: Optional

---

## Medium Models (7B–8B)

* RAM: 16 GB+
* GPU Recommended

---

## Large Models (14B+)

* RAM: 32 GB+
* Dedicated GPU Recommended

---

# 📚 Learning Outcomes

By exploring this project, you will learn:

* LangChain RAG Pipelines
* Retrieval-Augmented Generation (RAG)
* FAISS Vector Databases
* Ollama Integration
* YouTube Transcript API
* Embedding Models
* Semantic Search
* Prompt Engineering
* Local AI Applications
* Python Automation

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

* Improving transcript handling
* Supporting multiple videos
* Persistent FAISS storage
* Streamlit interface
* FastAPI backend
* Memory integration
* Playlist support
* Timestamp citations
* OCR support for subtitles
* Performance optimization

---

## 🙌 Author

**Zohaib Sattar**

📧 Email: [zabizubi86@gmail.com](mailto:zabizubi86@gmail.com)

🔗 LinkedIn: [https://www.linkedin.com/in/zohaib-sattar-5680ab2a5/](https://www.linkedin.com/in/zohaib-sattar-5680ab2a5/)

---

## ⭐ Support & Share the Project

If you found this project useful, consider:

* ⭐ Star this repository
* 🍴 Fork the repository
* 🛠️ Contribute improvements
* 📢 Share it with the AI community

Your support helps grow open-source AI projects and encourages future AI development.

---

# 📜 License

This project is open-source and available under the **MIT License**.
