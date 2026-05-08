
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")
text1 = "Python backend developer using APIs and databases"

text2 = "FastAPI engineer building backend REST APIs"

text3 = "Professional football player and sports athlete"

embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
embedding3 = model.encode(text3)

similarity_Python_FastApi = cosine_similarity(
    [embedding1],[embedding2]
)[0][0]

similarity_Python_Football = cosine_similarity(
    [embedding1],[embedding3]
)[0][0]

print("\n========== COSINE SIMILARITY ==========")

print(f"\nPython ↔ FastAPI:")

print(f"Similarity Score: {similarity_Python_FastApi:.4f}")

print(f"\nPython ↔ Football:")

print(f"Similarity Score: {similarity_Python_Football:.4f}")