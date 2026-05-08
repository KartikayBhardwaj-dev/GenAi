# 🧠 Week 3 — Embeddings + Vector Databases + Retrieval

This week focused on understanding how modern RAG (Retrieval-Augmented Generation) systems work internally using embeddings, vector databases, and similarity search.

---

# 📚 Concepts Covered

## 1. Embeddings

Learned how text is converted into dense numerical vectors.

### Key Understanding

- Similar meaning → vectors are close together
- Different meaning → vectors are far apart
- Embeddings capture semantic meaning, not exact words

### Experiments

Generated embeddings for:
- "Python backend developer"
- "FastAPI engineer"
- "Football player"

Observed:
- All vectors had same dimensions
- Embeddings are arrays of floating-point numbers
- Semantically related texts produce similar vectors

---

# 📐 Cosine Similarity

Learned how similarity between embeddings is measured.

### Key Understanding

Cosine similarity measures the angle between vectors:
- Closer angle → higher similarity
- Larger angle → lower similarity

### Experiments

Compared:
- Python ↔ FastAPI
- Python ↔ Football

Observed:
- Technical concepts had higher similarity
- Unrelated concepts had lower similarity

---

# 🗂 Vector Databases (FAISS)

Learned why traditional databases are not suitable for semantic search.

### Key Understanding

Normal databases:
- match keywords
- fail at semantic understanding

Vector databases:
- search using meaning
- retrieve semantically similar chunks

### Experiments

Built:
- PDF chunking pipeline
- Embedding generation pipeline
- FAISS vector index

Stored:
- document chunks as vectors

Observed:
- fast nearest-neighbor retrieval
- semantic chunk matching

---

# 🔍 Retrieval System

Learned how retrieval works internally in RAG systems.

### Key Understanding

Pipeline:
1. User query
2. Query embedding
3. Similarity search
4. Top-k chunk retrieval

### Experiments

Queried vector DB with:
- technical questions
- resume-related searches

Retrieved:
- top 3 similar chunks
- similarity scores

Observed:
- embeddings enable semantic search
- retrieval quality depends on chunk quality

---

# ⚠️ Retrieval Failure Cases

One of the most important concepts learned this week.

### Goal

Understand why retrieval systems sometimes fail.

### Experiments

Tested vague queries:
- "server-side APIs"
- "cloud deployment"
- "frontend framework"

### Observed Problems

- irrelevant chunks retrieved
- semantic misses
- missing context
- weak chunk boundaries

### Key Learning

Good retrieval depends on:
- chunking strategy
- embedding quality
- metadata
- query phrasing

This separated conceptual understanding from tutorial-level implementation.

---

# 💾 Chroma Vector Database

Learned persistent vector storage using Chroma.

### Key Understanding

Unlike FAISS in-memory indexing:
- Chroma can persist embeddings to disk
- embeddings can be reused without recomputation

### Experiments

Built:
- persistent Chroma DB
- reloadable retrieval system

Observed:
- vector DB survives script restart
- reusable semantic memory system

---

# 🛠 Technologies Used

- LangChain
- Sentence Transformers
- FAISS
- ChromaDB
- HuggingFace Embeddings
- RecursiveCharacterTextSplitter
- PyPDFLoader

---

# 📁 Implemented Systems

## ✅ Embedding Experiments
Generated and inspected embedding vectors manually.

## ✅ Similarity Search System
Compared semantic similarity using cosine similarity.

## ✅ FAISS Retrieval Pipeline
Created vector index and semantic retrieval workflow.

## ✅ Retrieval Failure Analysis
Tested edge cases and semantic retrieval weaknesses.

## ✅ Chroma Persistent Database
Stored and reloaded embeddings persistently.

---

# 🧠 Core Takeaways

By the end of Week 3, understood:

- how semantic search works
- why embeddings are foundational to modern AI systems
- how vector databases retrieve context
- why chunking quality matters
- why retrieval can fail
- how RAG systems retrieve relevant information before generation

This week built the conceptual foundation required for:
- RAG systems
- AI assistants
- semantic search engines
- document Q&A systems
- knowledge retrieval architectures

---