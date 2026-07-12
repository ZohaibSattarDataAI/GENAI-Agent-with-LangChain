# 😊 AI Sentiment Analysis using LangChain & Ollama

A production-ready **AI-powered Sentiment Analysis** project built with **LangChain**, **Ollama**, and **Large Language Models (LLMs)**.

This project enables users to analyze the **sentiment of any text** and classify it as **Positive, Negative, or Neutral** using a local Large Language Model. It leverages **LangChain Runnables**, **Prompt Engineering**, and **Ollama** to build a lightweight, modular, and completely offline sentiment analysis pipeline.

Whether you're working on customer reviews, social media analysis, product feedback, news articles, or NLP projects, this repository demonstrates how modern LLMs can perform accurate sentiment classification with just a few lines of code.

---

# 🚀 Overview

Understanding people's opinions from text is one of the most common Natural Language Processing (NLP) tasks. This AI Sentiment Analysis project automates that process by analyzing text and determining whether the expressed sentiment is positive, negative, or neutral.

The application uses **LangChain Runnable Chains** to create a clean and modular AI workflow that accepts user input, processes it through a prompt template, generates a response using an Ollama model, and returns the final sentiment classification.

Workflow:

```
User Text
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
Sentiment Result
```

This project is an excellent practical example of **Prompt Engineering**, **LangChain Runnables**, and **LLM-powered Natural Language Processing (NLP)**.

---

# ✨ Features

- 😊 AI-powered sentiment classification
- 🧠 Prompt Engineering with LangChain
- ⚡ Runnable Chains
- 🤖 Local LLM support using Ollama
- 📊 Positive, Negative, and Neutral prediction
- 📖 Sentiment explanation generation
- 📌 Structured AI responses
- 📝 Works with reviews, comments, tweets, and articles
- 📚 Beginner-friendly project
- 🔒 Completely offline execution
- 🖥️ Command-line interface (CLI)
- 🚀 Fast and lightweight architecture

---

# 📂 Project Structure

```
Sentiment-Analysis-using-LangChain/
│
├── sentiment_analysis.py
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

### Output Parsing

- StrOutputParser

### Prompt Engineering

- ChatPromptTemplate

---

# 🔄 LangChain Workflow

This project uses a simple and modular Runnable pipeline.

```
User Input
    │
    ▼
Prompt Template
    │
    ▼
ChatOllama
    │
    ▼
StrOutputParser
    │
    ▼
Sentiment Analysis Result
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
python sentiment_analysis.py
```

---

# 💻 Example

```
Enter Text:

I absolutely love this product. The quality is amazing and delivery was very fast.
```

---

Example Output

```
Sentiment:
Positive

Confidence:
High

Reason:
The text expresses strong satisfaction, appreciation, and positive emotions toward the product.
```

---

Another Example

```
Input:

The service was slow and the product arrived damaged.
```

Output

```
Sentiment:
Negative

Confidence:
High

Reason:
The text describes dissatisfaction due to poor service and a damaged product.
```

---

Another Example

```
Input:

The meeting will start tomorrow at 10 AM.
```

Output

```
Sentiment:
Neutral

Confidence:
Medium

Reason:
The text provides factual information without expressing emotion or opinion.
```

---

# 🧠 Concepts Covered

- LangChain
- Runnable Chains
- Prompt Engineering
- ChatPromptTemplate
- StrOutputParser
- Sentiment Analysis
- Natural Language Processing (NLP)
- Large Language Models
- Ollama
- AI Text Classification
- Python Automation

---

# 📈 Future Improvements

Planned features include:

- Streamlit GUI
- FastAPI Integration
- Batch Sentiment Analysis
- CSV File Analysis
- Excel File Support
- PDF Text Analysis
- Social Media Sentiment Dashboard
- REST API
- Emotion Detection
- Aspect-Based Sentiment Analysis
- Multi-language Sentiment Analysis
- Confidence Score Visualization
- Real-time Twitter/X Analysis
- Sentiment Charts
- Hugging Face Model Support

---

# 🤖 Recommended Ollama Models

For better sentiment analysis accuracy, use one of the following models.

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best overall sentiment analysis |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Accurate text understanding |
| gemma3:4b | ⭐⭐⭐⭐⭐ Natural language reasoning |
| mistral:7b | ⭐⭐⭐⭐⭐ Advanced NLP tasks |

---

## Fast Models

- qwen2.5:1.5b ⭐ Recommended
- llama3.2:1b
- gemma3:1b

Best for:

- 8 GB RAM
- Fast inference
- Learning LangChain
- Lightweight NLP applications

---

## Medium Models

- qwen2.5:3b ⭐ Recommended
- llama3.2:3b ⭐ Recommended
- gemma3:4b
- phi4-mini
- granite3.3

Best for:

- Customer feedback analysis
- Product review analysis
- Social media monitoring
- Daily NLP tasks

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

- Enterprise sentiment analysis
- Large-scale NLP pipelines
- Research projects
- High-accuracy text classification

---

# 🎯 Sentiment Analysis Applications

The generator can analyze:

- Product Reviews
- Customer Feedback
- Movie Reviews
- Social Media Posts
- Tweets
- News Articles
- Blog Comments
- Survey Responses
- Email Feedback
- Support Tickets
- Restaurant Reviews
- App Reviews
- Educational Feedback
- Business Reports
- Custom Text Input

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
- Sentiment Analysis
- Natural Language Processing (NLP)
- Large Language Models
- Ollama Integration
- AI Text Classification
- AI Workflow Design
- Python AI Applications
- Local LLM Deployment

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Improving prompts
- Adding emotion detection
- Supporting additional languages
- Streamlit UI
- FastAPI backend
- REST API
- CSV & Excel analysis
- Confidence score visualization
- Hugging Face integration
- Batch processing
- Dashboard development
- Performance optimization

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
