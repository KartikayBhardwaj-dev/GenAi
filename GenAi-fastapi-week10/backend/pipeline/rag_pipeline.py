from backend.utils.pdf_loader import (load_pdf)
from backend.utils.text_splitter import (split_text)
from backend.utils.embeddings import (load_embeddings)
from backend.vectorstore.build_vectorstore import (create_vectorstore)
from backend.retrievers.retriever import (retrieve_chunks)
from backend.chains.rag_chain import (rag_chain)
# ----------BUILD VECTORSTORE--------
def build_vectorstore(pdf_path):
    # --------LOAD PDF---------
    documents = load_pdf(pdf_path)

    # --------SPLIT TEXT------
    chunks = split_text(documents)

    # ----------EMBEDDINGS--------
    embeddings = load_embeddings()

    # ----------VECTORSTORE--------
    vectorstore = create_vectorstore(chunks=chunks, embeddings=embeddings)
    return vectorstore

# --------FORMAT SOURCES--------
def format_sources(results):
    sources = []
    for doc, score in results:
        source = {
            "page": doc.metadata.get("page"),
            "score": float(score),
            "content": doc.page_content
        }
        sources.append(source)
    return sources

# -------------ASK QUESTION-------------
def ask_question(question, vectorstore, k=3):
    # ---------RETRIEVE----------
    results = retrieve_chunks(vectorstore=vectorstore, query=question, k=k)

    # --------BUILD CONTEXT------------
    context = "\n\n".join([
        doc.page_content for doc, score in results
    ])

    # --------GENERATE ANSWER-----------
    answer = rag_chain.invoke({
        "context": context,
        "question": question
    })

    # -------FORMAT SOURCES------
    sources = format_sources(results)
    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }

# -------TEST---
if __name__ == "__main__":
    vectorstore = build_vectorstore("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-fastapi-week10/data/resume.pdf")
    question = ("What technologies are used?")

    response = ask_question(
        question=question,
        vectorstore=vectorstore,
        k=3
    )
    print("\nQUESTION:\n")
    print(response["question"])
    print("\nANSWER:\n")
    print(response["answer"])
    print("\nSOURCES:\n")

    for source in response["sources"]:
        print(source)