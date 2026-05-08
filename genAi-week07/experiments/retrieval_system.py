from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ------------------ LOAD PDF ------------------

file_path = "/Users/kartikaybhardwaj/Desktop/GenAi/genAi-week07/resume.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

# ------------------ SPLIT CHUNKS ------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(f"\nTotal Chunks: {len(chunks)}")

# ------------------ LOAD EMBEDDING MODEL ------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------ CREATE CHUNK EMBEDDINGS ------------------

texts = [chunk.page_content for chunk in chunks]
embeddings = model.encode(texts)
embedding_array = np.array(embeddings).astype("float32")

# ------------------ CREATE FAISS INDEX ------------------

dimension = embedding_array.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embedding_array)

print(f"\nVectors Stored: {index.ntotal}")


# ------------------QUERY-------------------------

query = "Python Backend api Development"
print(f"\nQuery: {query}")

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

# Search top K

k = 3

distances, indices = index.search(query_embedding, k)

# =========================================================

# PRINT RESULTS

# =========================================================

print("\n========== TOP RESULTS ==========")

for rank, idx in enumerate(indices[0]):
    print(f"\n--- Rank {rank+1} ---")
    print(f"Chunk Index: {idx}")
    print(f"Distance Score: {distances[0][rank]}")
    print("\nChunk Content:\n")
    print(chunks[idx].page_content)