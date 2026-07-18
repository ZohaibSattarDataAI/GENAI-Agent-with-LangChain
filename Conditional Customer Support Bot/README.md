# 📄 AI Customer Support Bot using LangChain & Ollama

A production-ready **AI-powered Customer Support Assistant** built with **LangChain**, **Ollama**, **Prompt Engineering**, **Conversation Memory**, and **Large Language Models (LLMs)**.

This project simulates an intelligent customer support representative capable of answering customer queries, resolving common issues, explaining products and services, and maintaining natural conversations.

Instead of waiting for a human agent, customers can instantly receive accurate, professional, and context-aware responses powered by a local LLM.

This project demonstrates how **LangChain**, **Prompt Templates**, **Runnable Chains**, **Conversation Memory**, and **Local LLMs** work together to build an AI-powered customer support chatbot.

---

# 🚀 Overview

Customer support is one of the most common real-world applications of Large Language Models.

This project uses **LangChain** and **Ollama** to create a conversational AI assistant capable of handling customer inquiries while maintaining conversation history for better responses.

The workflow is illustrated below:

```

             Customer

                 │

                 ▼

        Customer Question

                 │

                 ▼

        LangChain Prompt

                 │

                 ▼

      Conversation Memory

                 │

                 ▼

          Ollama LLM

                 │

                 ▼

      AI Customer Response

                 │

                 ▼

           Customer

```

This project is an excellent beginner-friendly implementation of an **AI Customer Support Chatbot** using LangChain.

---

# ✨ Features

- 🤖 AI-powered customer support
- 💬 Multi-turn conversations
- 🧠 Conversation memory
- 📦 Local LLM using Ollama
- ⚡ LangChain Runnable Chains
- 🔒 Fully offline execution
- 📝 Product & service assistance
- ❓ FAQ handling
- 🔄 Context-aware responses
- 😊 Friendly and professional replies
- 🖥️ Simple command-line interface (CLI)
- 🎯 Beginner-friendly architecture

---

# 📂 Project Structure

```

Customer-Support-Bot/

│

├── customer_support.py

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

### Prompt Engineering

- ChatPromptTemplate
- MessagesPlaceholder

### Memory

- Conversation History
- HumanMessage
- AIMessage

### Output Parser

- StrOutputParser

### Programming Language

- Python 3.10+

---

# 🔄 AI Workflow

This project follows a conversational AI pipeline.

```

Customer

 │

 ▼

User Question

 │

 ▼

Prompt Template

 │

 ▼

Conversation History

 │

 ▼

Ollama LLM

 │

 ▼

Generated Response

 │

 ▼

Customer

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
ollama pull qwen2.5:3b
```

---

## 6 Start Ollama

```bash
ollama serve
```

---

## 7 Run the Project

```bash
python customer_support.py
```

---

# 💻 Example

Start Conversation

```
Customer: Hi
```

---

Ask Questions

```
I forgot my password.

How can I reset my account?

What are your business hours?

How do I track my order?

Can I return my product?

What payment methods do you accept?

How can I contact support?
```

---

Example Output

```
Customer:

I forgot my password.

Support:

No problem!

You can reset your password by clicking the
"Forgot Password" option on the login page.

A password reset link will be sent to your registered email address.
```

---

# 🧠 Concepts Covered

- LangChain
- Prompt Engineering
- Runnable Chains
- Conversation Memory
- Chat Models
- Ollama
- Local LLMs
- AI Chatbots
- Customer Support Automation
- Context-aware Conversations

---

# 📈 Future Improvements

Planned features include:

- Streamlit Interface
- FastAPI Backend
- Web Chat Interface
- User Authentication
- Chat History Database
- RAG with Company FAQs
- Ticket Generation
- Email Notifications
- Voice Support
- Multi-language Support
- Sentiment Analysis
- Human Agent Handoff
- CRM Integration
- Analytics Dashboard

---

# 🤖 Recommended Ollama Models

For better performance, consider using the following models.

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best balance of speed and quality |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Excellent reasoning |
| gemma3:4b | ⭐⭐⭐⭐⭐ Natural conversations |
| mistral:7b | ⭐⭐⭐⭐⭐ Customer support |

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

- Customer support
- AI assistants
- Production prototypes
- Better conversations

---

## High-End Models

- qwen3:8b
- llama3.1:8b
- llama3.3:70b
- mistral-small:24b
- deepseek-r1:8b
- deepseek-r1:14b

Best for:

- Enterprise customer support
- Advanced reasoning
- Long conversations
- Large-scale deployments

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
- Prompt Engineering
- Runnable Chains
- AI Chatbots
- Conversation Memory
- Local LLM Deployment
- Ollama
- Customer Support Automation
- Prompt Design
- Context-aware AI Systems

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Improving prompts
- Adding memory backends
- Better conversation management
- Streamlit UI
- FastAPI integration
- Voice support
- CRM integration
- Ticket generation
- Analytics dashboard
- Multi-language support

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
