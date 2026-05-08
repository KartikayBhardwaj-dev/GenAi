from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week06/practice/resume.pdf")
docs = loader.load()
chunk_size = 500
chunk_overlap = 50
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

chunks = splitter.split_documents(docs)
print("\n========== BASIC SPLIT ==========")

print(f"Chunk Size: {chunk_size} | Overlap: {chunk_overlap}")

print(f"Total Chunks: {len(chunks)}")

# ------------------ PRINT FIRST 2 CHUNKS ------------------

for i, chunk in enumerate(chunks[:2]):

    print(f"\n--- Chunk {i+1} ---")

    print(chunk.page_content.strip())

    print("\nLength:", len(chunk.page_content))

    print("Metadata:", chunk.metadata)

# ------------------ EXTRA (GOOD PRACTICE) ------------------

avg_length = sum(len(c.page_content) for c in chunks) / len(chunks)

print(f"\nAverage Chunk Length: {int(avg_length)}")



 

