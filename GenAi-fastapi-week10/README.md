# 📄 Conversational PDF RAG System

A production-style Conversational RAG (Retrieval-Augmented Generation) application built using:

- FastAPI
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq LLM
- Conversational Memory
- Session-based Chat

---

# 🚀 Features

✅ Upload PDFs  
✅ Ask questions from PDFs  
✅ Conversational memory  
✅ Multi-turn chat  
✅ Session isolation  
✅ Standalone question generation  
✅ FastAPI backend  
✅ Streamlit frontend  
✅ Source retrieval display  
✅ FAISS vector search  
✅ Production-style architecture

---

# 🧠 Architecture

```text
Streamlit Frontend
        ↓
FastAPI APIs
        ↓
Conversational Pipeline
        ↓
Retriever
        ↓
FAISS Vector Store
        ↓
Groq LLM
```

---

# 📁 Project Structure

```text
backend/
│
├── api/
│   ├── main.py
│   ├── routes/
│   │   ├── upload_routes.py
│   │   ├── ask_routes.py
│   │   └── chat_routes.py
│   │
│   └── schemas/
│       ├── request_schema.py
│       └── response_schema.py
│
├── chains/
│   └── conversational_chain.py
│
├── memory/
│   └── memory_manager.py
│
├── pipeline/
│   ├── rag_pipeline.py
│   └── conversational_pipeline.py
│
├── retrievers/
│   ├── retriever.py
│   └── history_aware_retriever.py
│
├── utils/
│   ├── embeddings.py
│   ├── pdf_loader.py
│   ├── session_manager.py
│   ├── text_splitter.py
│   ├── topic_extraction.py
│   └── rewrite_validator.py
│
├── vectorstore/
│   └── build_vectorstore.py
│
frontend/
│
└── app.py
│
uploads/
│
requirements.txt
README.md
.env
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>

cd conversational-rag
```

---

## 2️⃣ Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn backend.api.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 📤 Upload API

## Endpoint

```http
POST /upload
```

## Form Data

```text
file: PDF
session_id: string
```

## Flow

```text
Upload PDF
    ↓
Save File
    ↓
Load PDF
    ↓
Split Chunks
    ↓
Generate Embeddings
    ↓
Create FAISS
    ↓
Store In Session
```

---

# ❓ Ask API

## Endpoint

```http
POST /ask
```

## Request

```json
{
  "question": "What is LangChain?",
  "session_id": "abc123"
}
```

## Response

```json
{
  "question": "What is LangChain?",
  "standalone_question": "What is LangChain?",
  "answer": "LangChain is...",
  "sources": []
}
```

---

# 💬 Conversational Chat API

## Endpoint

```http
POST /chat
```

## Request

```json
{
  "question": "Who created it?",
  "session_id": "abc123"
}
```

## Conversational Flow

```text
User Question
        ↓
Chat History
        ↓
Standalone Question
        ↓
Retriever
        ↓
Context
        ↓
LLM
        ↓
Answer
```

---

# 🧠 Conversational Memory

The application stores:

```python
{
    session_id: {
        vectorstore,
        memory,
        topic
    }
}
```

This enables:

✅ Session isolation  
✅ Multi-user support  
✅ Conversational context  
✅ Topic continuity

---

# 🔎 Retrieval Pipeline

```text
Question
    ↓
Standalone Rewrite
    ↓
Similarity Search
    ↓
Retrieve Top K Chunks
    ↓
Build Context
    ↓
Generate Response
```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- LangChain
- FAISS
- HuggingFace
- Groq

## Frontend

- Streamlit

## Embeddings

- sentence-transformers

## Vector Database

- FAISS

---

# 📦 requirements.txt

```txt
langchain==0.2.16
langchain-core==0.2.43
langchain-community==0.2.16
langchain-text-splitters==0.2.4
langchain-groq==0.1.9
langchain-huggingface==0.0.3

groq==0.9.0
httpx==0.27.2

sentence-transformers==3.0.1
transformers==4.43.4
tokenizers==0.19.1

faiss-cpu==1.8.0.post1

pypdf==4.3.1

fastapi==0.115.0
uvicorn==0.30.6
python-multipart==0.0.9

streamlit==1.38.0

python-dotenv==1.0.1

pydantic==2.8.2

numpy==1.26.4
pandas==2.2.2
requests==2.32.3

tiktoken==0.7.0

loguru==0.7.2
```

---

# ✅ Current Capabilities

✅ PDF Upload  
✅ Semantic Search  
✅ RAG Pipeline  
✅ Conversational RAG  
✅ Multi-turn Memory  
✅ Session-based Chat  
✅ FastAPI APIs  
✅ Streamlit Frontend  
✅ Source Citations

---

# 🚀 Future Improvements

- Persistent database
- Redis session storage
- PostgreSQL integration
- Docker deployment
- Authentication
- Streaming responses
- Async pipelines
- Cloud deployment
- Multi-PDF support
- Agent workflows
- Evaluation pipelines

---

# 📚 Learning Outcomes

This project teaches:

✅ Production RAG  
✅ Conversational AI  
✅ FastAPI  
✅ Vector Databases  
✅ Embeddings  
✅ Session Management  
✅ API Architecture  
✅ Memory Systems  
✅ Frontend Integration  
✅ Deployable AI Systems

---

# 👨‍💻 Author

Built as a production-style GenAI engineering project.