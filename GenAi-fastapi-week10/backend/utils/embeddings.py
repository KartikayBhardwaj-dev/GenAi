from langchain_huggingface import (HuggingFaceEmbeddings)
from backend.config import (EMBEDDING_MODEL)
# ---------LOAD EMBEDDINGS------------

def load_embeddings():
    embeddings = (
        HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )
    )
    return embeddings
