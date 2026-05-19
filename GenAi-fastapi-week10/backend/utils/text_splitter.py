from langchain_text_splitters import (RecursiveCharacterTextSplitter)

from backend.config import ( CHUNK_OVERLAP, CHUNK_SIZE)

# --------SPLIT TEXT-----------
def split_text(documents):
    splitter = (RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    ))

    chunks = splitter.split_documents(documents)
    return chunks