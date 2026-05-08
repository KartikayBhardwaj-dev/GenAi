print("Starting script...")
from langchain_community.document_loaders import PyPDFLoader
print("PDF loader imported...")
from langchain_text_splitters import RecursiveCharacterTextSplitter
print("Splitter imported...")
from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

# --------------Load PDF-----------------------------------------
file_path = "/Users/kartikaybhardwaj/Desktop/GenAi/genAi-week07/resume.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
print(f"\nTotal no of pages: {len(docs)}")

# --------------Split Chunks-----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
    
)

chunks = splitter.split_documents(docs)
print(f"Total no of Chunks: {len(chunks)}")

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)

# ------------------Create Chroma db-----------------------------
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

print("\nEmbeddings stored in Chroma DB")
print(f"\nTotal Chunks Stored: {len(chunks)}")