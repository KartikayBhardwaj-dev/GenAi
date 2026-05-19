from backend.utils.pdf_loader import (

    load_pdf

)

from backend.utils.rewrite_validator import (

    validate_rewrite

)

from backend.utils.text_splitter import (

    split_text

)

from backend.utils.embeddings import (

    load_embeddings

)

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

from backend.memory.memory_manager import (

    get_chat_history,

    add_user_message,

    add_ai_message,

    format_chat_history,

    get_current_topic,

    set_current_topic

)

from backend.utils.topic_extraction import (

    extract_topic

)

from backend.utils.session_manager import (

    set_vectorstore,

    get_vectorstore

)

# ============================================================

# ---------- BUILD CONTEXT ----------

# ============================================================

def build_context(results):

    if not results:

        return ""

    contexts = []

    for i, (doc, score) in enumerate(results):

        content = doc.page_content.strip()

        if len(content) > 20:

            contexts.append(

                f"""

SOURCE {i+1}

Relevance Score:

{round(score, 4)}

CONTENT:

{content}

"""

            )

    return "\n\n".join(contexts)

# ============================================================

# ---------- BUILD VECTORSTORE ----------

# ============================================================

def build_vectorstore(

    pdf_path,

    session_id

):

    # ---------- LOAD PDF ----------

    documents = load_pdf(

        pdf_path

    )

    # ---------- SPLIT CHUNKS ----------

    chunks = split_text(

        documents

    )

    # ---------- LOAD EMBEDDINGS ----------

    embeddings = load_embeddings()

    # ---------- CREATE VECTORSTORE ----------

    vectorstore = create_vectorstore(

        chunks=chunks,

        embeddings=embeddings

    )

    # ---------- STORE VECTORSTORE IN SESSION ----------

    set_vectorstore(

        session_id=session_id,

        vectorstore=vectorstore

    )

    return vectorstore

# ============================================================

# ---------- FORMAT SOURCES ----------

# ============================================================

def format_sources(results):

    sources = []

    for doc, score in results:

        source = {

            "page": doc.metadata.get(

                "page"

            ),

            "score": float(score),

            "content": doc.page_content

        }

        sources.append(source)

    return sources

# ============================================================

# ---------- ASK QUESTION ----------

# ============================================================

def ask_question(

    question,

    session_id,

    k=3

):

    # ---------- GET VECTORSTORE ----------

    vectorstore = get_vectorstore(

        session_id

    )

    if vectorstore is None:

        return {

            "error": "No PDF uploaded for this session."

        }

    # ---------- MEMORY ----------

    chat_history = get_chat_history(

        session_id

    )

    history_text = format_chat_history(

        chat_history

    )

    current_topic = get_current_topic(

        session_id

    )

    # ---------- STANDALONE QUESTION ----------

    standalone_question = (

        generate_standalone_question(

            question=question,

            chat_history=history_text,

            current_topic=current_topic

        )

    )

    print(

        "\nStandalone Question:"

    )

    print(

        standalone_question

    )

    # ---------- VALIDATE REWRITE ----------

    is_valid = validate_rewrite(

        original_question=question,

        rewritten_question=standalone_question

    )

    if not is_valid:

        print(

            "\nInvalid rewrite detected."

        )

        standalone_question = question

        print(

            "Fallback to original question:"

        )

        print(

            standalone_question

        )

    # ---------- TOPIC EXTRACTION ----------

    new_topic = extract_topic(

        standalone_question

    )

    set_current_topic(

        session_id,

        new_topic

    )

    # ---------- RETRIEVE ----------

    results = retrieve_chunks(

        vectorstore=vectorstore,

        query=standalone_question,

        k=k

    )

    # ---------- DEBUG RETRIEVAL ----------

    print(

        "\n========== RETRIEVED CHUNKS ==========\n"

    )

    for i, (doc, score) in enumerate(results):

        print(

            f"\nCHUNK {i+1}"

        )

        print(

            f"SCORE: {score}"

        )

        print(

            doc.page_content[:700]

        )

    # ---------- BUILD CONTEXT ----------

    context = build_context(

        results

    )

    # ---------- EMPTY CONTEXT GUARD ----------

    if not context.strip():

        answer = (

            "I could not find relevant "

            "information from the uploaded document."

        )

    else:

        # ---------- GENERATE ANSWER ----------

        answer = conversational_chain.invoke({

            "chat_history": history_text,

            "context": context,

            "question": question

        })

    # ---------- SAVE MEMORY ----------

    add_user_message(

        session_id=session_id,

        message=question

    )

    add_ai_message(

        session_id=session_id,

        message=answer

    )

    # ---------- FORMAT SOURCES ----------

    sources = format_sources(

        results

    )

    return {

        "question": question,

        "standalone_question":

            standalone_question,

        "answer": answer,

        "sources": sources

    }