# 📄 Chat With Your PDF — Full Stack RAG Application

A ChatGPT-like PDF Question Answering System built using LangChain, FAISS, HuggingFace Embeddings, Groq LLMs, and Streamlit.

Upload any PDF and ask natural language questions about the document.

The system retrieves relevant chunks using semantic search and generates grounded answers using Retrieval-Augmented Generation (RAG).

---

# 🚀 Features

✅ Upload any PDF  
✅ Semantic chunk retrieval  
✅ FAISS vector database  
✅ HuggingFace embeddings  
✅ Grounded LLM answers  
✅ “I don’t know” hallucination prevention  
✅ Source citation with page references  
✅ ChatGPT-style Streamlit UI  
✅ End-to-end RAG pipeline  
✅ Retrieval-based semantic search

---

# 🧠 How It Works

```text
Upload PDF
    ↓
PDF Loading
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Store
    ↓
User Question
    ↓
Similarity Search
    ↓
Context Retrieval
    ↓
Prompt Grounding
    ↓
LLM Answer Generation
```

---

# 🛠 Tech Stack

## Backend
- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq API

## Frontend
- Streamlit

## LLM
- Llama 3.1 8B Instant (Groq)

## Embedding Model
- sentence-transformers/all-MiniLM-L6-v2

---

# 📂 Project Structure

```text
project/
│
├── backend/
│   ├── chains/
│   ├── pipeline/
│   ├── prompts/
│   ├── utils/
│   └── vectorstore/
│
├── frontend/
│   └── app.py
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd <repo_name>
```

---

## 2. Create Virtual Environment

```bash
python3.10 -m venv venv
```

### Activate Environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

---

# ▶️ Run Application

From the project root directory:

```bash
streamlit run frontend/app.py
```

---

# 💬 Example Questions

```text
Summarize this PDF
Explain chapter 2
What technologies are mentioned?
Give key concepts from this lecture
What is retrieval augmented generation?
```

---

# 📸 Use Cases

- Lecture Notes QA
- Research Paper Assistant
- Resume Analyzer
- Documentation Chatbot
- Book Summarizer
- Knowledge Base Assistant

---

# 🧩 Key Concepts Implemented

✅ PDF Loading  
✅ Recursive Text Chunking  
✅ Embedding Generation  
✅ Vector Databases (FAISS)  
✅ Semantic Retrieval  
✅ Prompt Grounding  
✅ Hallucination Prevention  
✅ Source Citation  
✅ Full Stack RAG Pipeline

---

# 🧠 Learning Outcomes

This project helped me understand:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Prompt Engineering
- Grounded LLM Responses
- LangChain LCEL Pipelines
- Full Stack GenAI Architecture
- Streamlit Frontend Integration

---

# 🚀 Future Improvements

- Persistent FAISS storage
- FastAPI backend
- Conversational memory
- Streaming responses
- Docker deployment
- Cloud deployment
- Hybrid retrieval
- Reranking pipelines

---

# 📄 License

MIT License