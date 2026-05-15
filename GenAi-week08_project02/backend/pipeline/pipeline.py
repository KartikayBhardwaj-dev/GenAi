# ---------------- IMPORTS ----------------

from backend.utils.pdf_loader import load_pdf
from backend.utils.text_splitter import split_text
from backend.utils.embeddings import load_embeddings

from backend.vectorstore.build_vectorestore import create_vectorstore
from backend.vectorstore.retriever import retrieve_chunks

from backend.chains.chain import chain

# ---------------- BUILD VECTORSTORE ----------------

def build_vectorstore(pdf_path):

    # LOAD PDF
    documents = load_pdf(pdf_path)

    # SPLIT TEXT
    chunks = split_text(documents)

    # LOAD EMBEDDINGS
    embeddings = load_embeddings()

    # CREATE VECTORSTORE
    vectorstore = create_vectorstore(
        chunks=chunks,
        embeddings=embeddings
    )

    return vectorstore

# ---------------- FORMAT CONTEXT ----------------

def format_context(results):

    context = "\n\n".join([
        doc.page_content for doc, score in results
    ])

    return context

# ---------------- FORMAT SOURCES ----------------

def format_sources(results):

    if not results:
        return []

    # FAISS returns LOWER score = better match
    best_doc, best_score = results[0]

    source_data = {
        "page": best_doc.metadata.get("page"),
        "score": float(best_score),
        "content": best_doc.page_content
    }

    return [source_data]

# ---------------- MAIN QA FUNCTION ----------------

def ask_question(question, vectorstore, k=3):

    # RETRIEVE CHUNKS
    results = retrieve_chunks(
        vectorstore=vectorstore,
        query=question,
        k=k
    )

    # BUILD CONTEXT
    context = format_context(results)

    # GENERATE ANSWER
    answer = chain.invoke({
        "context": context,
        "question": question
    })

    # SOURCES
    sources = format_sources(results)

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": results
    }