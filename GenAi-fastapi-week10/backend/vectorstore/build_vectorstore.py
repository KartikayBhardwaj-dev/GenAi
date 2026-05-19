from langchain_community.vectorstores import (FAISS)

# ----------CREATE VECTORSTORE-------------
def create_vectorstore(chunks, embeddings):
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore