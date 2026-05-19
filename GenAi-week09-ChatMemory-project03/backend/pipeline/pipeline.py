from backend.utils.pdf_loader import load_pdf
from backend.utils.text_splitter import split_text
from backend.utils.embeddings import load_embeddings
from backend.vectorstore.build_vectorstore import (create_vectorstore)
from backend.retrievers.retriever import (retrieve_chunks)
from backend.chains.memory_chain import (
    memory_chain
)
from backend.memory.buffer_memory import (
    add_user_message,
    add_ai_message,
    get_chat_history
)

# --------------LOAD PDF-------------------
documents = load_pdf("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week09-ChatMemory-project03/data/resume.pdf")
print(f"\nLoaded Pages: {len(documents)}")

# ---------------SPLIT TEXT------------------------
chunks = split_text(documents)
print(f"\nTotal chunks: {len(chunks)}")

# ------------------EMBEDDINGS-----------------
embeddings = load_embeddings()
print("\nEmbeddings Loaded")

# ----------------VECTORSTORE-----------------
vectorstore = create_vectorstore(
    chunks=chunks,
    embeddings=embeddings
)
print("\nFAISS Vectorstore Created")

# ----------------QA FUNCTION----------------
def ask_question(question):
    results = retrieve_chunks(
        vectorstore=vectorstore,
        query=question,
        k=3
    )
    context = "\n\n".join([
        doc.page_content for doc, score in results
    ])
    history = get_chat_history()
    answer = memory_chain.invoke({
        "chat_history": history,
        "context": context,
        "question": question
    })

    add_user_message(question)
    add_ai_message(answer)

    return answer
# ------------------ TESTING ------------------

if __name__ == "__main__":

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":

            break

        answer = ask_question(question)

        print("\nAnswer:\n")

        print(answer)