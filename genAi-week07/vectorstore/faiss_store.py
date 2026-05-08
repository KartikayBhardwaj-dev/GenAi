from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from sentence_transformers import SentenceTransformer

import faiss
import numpy as np

file_path = "/Users/kartikaybhardwaj/Desktop/GenAi/genAi-week07/resume.pdf"

loader = PyPDFLoader(file_path)
docs = loader.load()
print(f"\nTotal Pages loaded: {len(docs)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)
print(f"\nTotal chunks created: {len(chunks)}")

model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [chunk.page_content for chunk in chunks]

embeddings = model.encode(texts)
print(f"\n Total embeddings created: {len(embeddings)}")

# ----------------Convert To Numpy----------------------
embedding_array = np.array(embeddings).astype("float32")

# -------------Create Faiss Index-------------------------
dimension = embedding_array.shape[1]
index = faiss.IndexFlatL2(dimension)

# -----------------store vectors------------------------
index.add(embedding_array)

print("\n========== FAISS INFO ==========")

print(f"Vector Dimension: {dimension}")

print(f"Number of Vectors Stored: {index.ntotal}")
