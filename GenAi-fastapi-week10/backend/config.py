import os 
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# --------API KEYS----------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------MODEL---------------
LLM_MODEL = "llama-3.1-8b-instant"
EMBEDDING_MODEL = ("sentence-transformers/all-MiniLM-L6-v2")

# ------------CHUNKING-------------

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 250

# ----------RETRIEVAL----------
TOP_K = 3
