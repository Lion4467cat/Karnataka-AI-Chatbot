# 🤖 Karnataka AI Chatbot

A domain-constrained LLM chatbot built with LangFlow, Groq API, and LLaMA 3.1 — designed to answer queries about Karnataka government services and information. Demonstrates how open-source LLMs can be deployed for specific knowledge domains without sending data to third-party APIs.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![LangFlow](https://img.shields.io/badge/LangFlow-Pipeline-FF6B6B?style=flat)
![Groq](https://img.shields.io/badge/Groq_API-LLaMA_3.1-00A67E?style=flat)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=flat)

---

## 🔍 What It Does

A general-purpose LLM like ChatGPT knows *everything* — which means it also hallucinates confidently about regional government specifics. This chatbot is constrained to a curated Karnataka knowledge base, so it only answers what it actually knows.

**Example queries it handles:**
- *"How do I apply for a caste certificate in Karnataka?"*
- *"What documents are needed for Aadhaar address change in Bangalore?"*
- *"List the Seva Sindhu services available online."*

---

## 🏗️ Architecture

```
User Query
    │
    ▼
LangFlow Pipeline
    │
    ├── Prompt Template (domain constraints)
    ├── Karnataka Knowledge Base (curated docs)
    └── Groq API → LLaMA 3.1 (inference)
    │
    ▼
Grounded Response
(constrained to Karnataka context only)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Groq API key → [console.groq.com](https://console.groq.com)
- LangFlow installed

### Installation

```bash
git clone https://github.com/Lion4467cat/Karnataka-AI-Chatbot.git
cd Karnataka-AI-Chatbot
pip install -r requirements.txt
```

### Configuration

Set your Groq API key:
```bash
export GROQ_API_KEY="your_key_here"
```

### Run

```bash
python app.py
```

---

## 🛠️ Tech Stack

- **LLM** — LLaMA 3.1 via Groq API
- **Pipeline** — LangFlow, LangChain
- **Backend** — Flask / Python
- **Knowledge Base** — Karnataka government documents

---

## 💡 Key Design Decision

This project deliberately uses **LLaMA 3.1 (open-source)** via Groq instead of OpenAI — demonstrating that domain-specific chatbots can be built without proprietary APIs, keeping costs near zero and data fully private. This is the architecture pattern used for enterprise deployments where data cannot leave the organization.

---

## 🔧 Adaptable For

This same architecture can be reused for any domain:
- Hospital FAQ chatbot
- College admissions assistant
- Legal document Q&A
- Product support bot

---

## 👤 Author

**S. S. Gokula Swamy** — [LinkedIn](https://www.linkedin.com/in/ssgokulaswamy) · [Portfolio](https://lion4467cat.github.io/raikabuilds)
