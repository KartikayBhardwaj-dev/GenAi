from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "FastApi Engineer",
    "Python Developer",
    "Football Player"
]

embeddings = model.encode(texts)

print("\n========== EMBEDDING EXPERIMENT ==========")

for i, embedding in enumerate(embeddings):

    print(f"\nText: {texts[i]}")

    # Vector dimension

    print(f"Vector Length: {len(embedding)}")

    # First 10 values

    print("\nFirst 10 Values:")

    print(embedding[:10])

    # Data type

    print("\nType:")

    print(type(embedding))