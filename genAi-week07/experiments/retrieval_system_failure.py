from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -------------------Load Pdf------------------
file_path = "/Users/kartikaybhardwaj/Desktop/GenAi/genAi-week07/resume.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [chunk.page_content for chunk in chunks]

embeddings = model.encode(texts)
embeddings_array = np.array(embeddings).astype("float32")

dimension = embeddings_array.shape[1]
index =faiss.IndexFlatL2(dimension)

# ----------------------Queries---------------
queries = [
    "server-side APIs",
    "cloud deployment",
    "frontend framework"
]

# ---------------Query embeddingss------------
for query in queries:
    print("\n================================================")
    print(f"QUERY: {query}")
    print("================================================")

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # ------------Search---------------------
    k = 3
    distances, indices = index.search(query_embedding, k)

    # ------------------ RESULTS ------------------

    for rank, idx in enumerate(indices[0]):
        print(f"\n--- Rank {rank+1} ---")
        print(f"Distance: {distances[0][rank]}")
        print("\nChunk:\n")
        print(chunks[idx].page_content[:500])