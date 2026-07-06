# ✍️ AI Blog Generator using LangChain & Ollama

A production-ready **AI-powered Blog Generator** built with **LangChain**, **Ollama**, and **Large Language Models (LLMs)**.

This project enables users to generate **high-quality, SEO-friendly, engaging, and well-structured blog articles** from a simple topic or prompt. It leverages **LangChain Runnables**, **Prompt Engineering**, and **Local LLMs** to automate professional content creation for blogs, websites, marketing campaigns, and educational content.

Whether you're a content creator, marketer, student, or developer, this project demonstrates how modern AI can streamline long-form content generation.

---

# 🚀 Overview

Creating high-quality blog content manually can be time-consuming. This AI Blog Generator simplifies the process by transforming a simple topic into a complete, well-organized blog article in seconds.

The application uses **LangChain Runnable Chains** to build a modular and maintainable AI pipeline that generates structured blog posts with titles, introductions, headings, conclusions, and SEO-friendly content.

Workflow:

```
User Topic
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
Generated Blog
```

This project is an excellent practical example of **Prompt Engineering**, **LangChain Runnables**, and **AI-powered content generation**.

---

# ✨ Features

- ✍️ AI-generated blog articles
- 🧠 Prompt Engineering with LangChain
- ⚡ Runnable Chains
- 🤖 Local LLM support using Ollama
- 📖 Long-form content generation
- 📰 Automatic blog title generation
- 📑 SEO-friendly article structure
- 📌 Automatic headings and subheadings
- 🎯 Keyword-focused content creation
- 📚 Beginner-friendly project
- 🔒 Completely offline execution
- 🖥️ Command-line interface (CLI)
- 🚀 Fast and lightweight architecture

---

# 📂 Project Structure

```
Blog-Generator-using-LangChain/
│
├── blog_generator.py
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
Generated Blog
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
python blog_generator.py
```

---

# 💻 Example

```
Enter Blog Topic:

Artificial Intelligence in Healthcare

Blog Tone:

Professional

Target Audience:

Students

Word Count:

1000
```

---

Example Output

```
Title:
The Future of Artificial Intelligence in Healthcare

Introduction

Artificial Intelligence (AI) is transforming the healthcare industry by improving diagnosis, treatment planning, patient care, and operational efficiency.

Main Sections

• What is Artificial Intelligence?
• Applications in Healthcare
• Benefits of AI
• Challenges and Limitations
• Future Trends

Conclusion

AI continues to reshape modern healthcare by enabling faster decision-making, improving patient outcomes, and reducing operational costs.
```

---

# 🧠 Concepts Covered

- LangChain
- Runnable Chains
- Prompt Engineering
- ChatPromptTemplate
- StrOutputParser
- AI Content Generation
- Large Language Models
- Ollama
- Long-form Text Generation
- SEO Content Writing
- Python Automation

---

# 📈 Future Improvements

Planned features include:

- Streamlit GUI
- FastAPI Integration
- Export Blog as PDF
- Export Blog as DOCX
- Markdown Export
- HTML Export
- Blog History
- Multiple Writing Styles
- AI Content Rewriting
- SEO Score Analysis
- Grammar Checker
- Keyword Density Analysis
- AI Content Humanizer
- Multi-language Blog Generation
- AI Image Generation
- One-click Publish to WordPress
- Medium Integration

---

# 🤖 Recommended Ollama Models

For better content quality, use one of the following models.

## ⭐ Best Overall

| Model | Recommended For |
|---------|----------------|
| qwen2.5:3b | ⭐⭐⭐⭐⭐ Best overall content generation |
| llama3.2:3b | ⭐⭐⭐⭐⭐ Professional blog writing |
| gemma3:4b | ⭐⭐⭐⭐⭐ Natural writing |
| mistral:7b | ⭐⭐⭐⭐⭐ Long-form articles |

---

## Fast Models

- qwen2.5:1.5b
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

Best for:

- Daily content creation
- SEO blog writing
- Educational articles
- Marketing content

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

- Professional blogging
- Enterprise content generation
- Long-form technical writing
- High-quality SEO articles

---

# 🎯 Blog Generation Options

The generator can create:

- Technology Blogs
- AI & Machine Learning Articles
- Programming Tutorials
- Travel Blogs
- Health & Fitness Blogs
- Educational Content
- Product Reviews
- Business Blogs
- Finance Articles
- Marketing Content
- News Summaries
- Research Articles
- Personal Blogs
- Lifestyle Blogs
- Custom Blog Topics

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
- AI Blog Generation
- Large Language Models
- Ollama Integration
- Python AI Applications
- SEO-friendly Content Creation
- AI Workflow Design
- Content Automation
- Prompt Optimization

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Adding new blog templates
- Improving prompts
- Optimizing AI-generated content
- Supporting additional export formats
- Streamlit UI
- FastAPI backend
- SEO optimization tools
- AI plagiarism checker
- AI summarization
- AI image generation
- WordPress publishing integration

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
