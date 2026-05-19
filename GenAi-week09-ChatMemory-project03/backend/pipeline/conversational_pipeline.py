from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

from backend.utils.pdf_loader import load_pdf
from backend.utils.text_splitter import split_text
from backend.utils.embeddings import load_embeddings
from backend.utils.logger import logger

from backend.vectorstore.build_vectorstore import (
    create_vectorstore
)

from backend.retrievers.retriever import (
    retrieve_chunks
)

from backend.retrievers.history_aware_retriever import (
    generate_standalone_question
)

from backend.chains.conversational_chain import (
    conversational_chain
)

# ------------------ CHAT HISTORY ------------------

chat_history = []

# ------------------ BUILD VECTORSTORE ------------------

def build_vectorstore(pdf_path):

    # ---------- LOAD PDF ----------

    documents = load_pdf(pdf_path)

    # ---------- SPLIT TEXT ----------

    chunks = split_text(documents)

    # ---------- EMBEDDINGS ----------

    embeddings = load_embeddings()

    # ---------- VECTORSTORE ----------

    vectorstore = create_vectorstore(
        chunks=chunks,
        embeddings=embeddings
    )

    return vectorstore

# ------------------ FORMAT CHAT HISTORY ------------------

def format_chat_history(
    chat_history,
    max_messages=6
):

    recent_messages = (
        chat_history[-max_messages:]
    )

    history = ""

    for message in recent_messages:

        history += (
            f"{message.type}: "
            f"{message.content}\n"
        )

    return history

# ------------------ FORMAT SOURCES ------------------

def format_sources(results):

    sources = []

    for doc, score in results:

        source_data = {
            "page": doc.metadata.get("page"),
            "score": score,
            "content": doc.page_content
        }

        sources.append(source_data)

    return sources

# ------------------ ASK QUESTION ------------------

def ask_question(

    question,

    vectorstore,

    k=3

):

    try:

        logger.info(

            f"Question: {question}"

        )

        standalone_question = (

            generate_standalone_question(

                question=question,

                chat_history=chat_history

            )

        )

        results = retrieve_chunks(

            vectorstore=vectorstore,

            query=standalone_question,

            k=k

        )

        context = "\n\n".join([

            doc.page_content

            for doc, score in results

        ])

        history_text = (

            format_chat_history(

                chat_history

            )

        )

        answer = conversational_chain.invoke({

            "chat_history": history_text,

            "context": context,

            "question": question

        })

        chat_history.append(

            HumanMessage(content=question)

        )

        chat_history.append(

            AIMessage(content=answer)

        )

        sources = format_sources(results)

        logger.info(

            "Answer generated successfully"

        )

        return {

            "answer": answer,

            "sources": sources

        }

    except Exception as e:

        logger.error(

            f"Error: {str(e)}"

        )

        return {

            "answer": (

                "Something went wrong."

            ),

            "sources": []

        }

# ------------------ TERMINAL TEST ------------------

if __name__ == "__main__":

    vectorstore = build_vectorstore(
        "/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week09-ChatMemory-project03/data/resume.pdf"
    )

    while True:

        question = input(
            "\nAsk Question: "
        )

        if question.lower() == "exit":
            break

        response = ask_question(
            question=question,
            vectorstore=vectorstore
        )

        print("\nAnswer:\n")

        print(response["answer"])