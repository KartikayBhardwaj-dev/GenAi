import sys
import os

# ------------------ PATH SETUP ------------------

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# ------------------ ENV ------------------

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# ------------------ IMPORTS ------------------

import tempfile
import streamlit as st

from backend.pipeline.conversational_pipeline import (
    build_vectorstore,
    ask_question
)

# ------------------ PAGE CONFIG ------------------

st.set_page_config(
    page_title="Conversational PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Conversational PDF Chatbot")

# ------------------ SIDEBAR ------------------

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    # ---------- RESET CHAT ----------

    if st.button("🗑 Reset Chat"):

        st.session_state.messages = []

        st.success("Chat Reset Successful ✅")

    st.markdown("---")

    st.markdown(
        """
        ### About
        
        Conversational RAG chatbot with:
        
        ✅ PDF Question Answering  
        ✅ Conversational Memory  
        ✅ History-Aware Retrieval  
        ✅ Source Grounding  
        """
    )

# ------------------ SESSION STATE ------------------

if "vectorstore" not in st.session_state:

    st.session_state.vectorstore = None

if "messages" not in st.session_state:

    st.session_state.messages = []

# ------------------ PDF UPLOAD ------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# ------------------ PROCESS PDF ------------------

if uploaded_file is not None:

    # ---------- PREVENT REPROCESSING ----------

    if (
        "uploaded_filename"
        not in st.session_state
        or st.session_state.uploaded_filename
        != uploaded_file.name
    ):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                uploaded_file.read()
            )

            temp_path = temp_file.name

        with st.spinner(
            "Processing PDF..."
        ):

            try:

                st.session_state.vectorstore = (
                    build_vectorstore(
                        pdf_path=temp_path
                    )
                )

                st.session_state.uploaded_filename = (
                    uploaded_file.name
                )

                st.success(
                    "PDF Processed Successfully ✅"
                )

            except Exception as e:

                st.error(
                    f"Error processing PDF: {str(e)}"
                )

# ------------------ DISPLAY CHAT HISTORY ------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        # ---------- SOURCES ----------

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            with st.expander(
                "View Sources"
            ):

                for source in message["sources"]:

                    st.markdown(
                        f"""
                        ### 📄 Source

                        **Page:** {source['page']}

                        **Score:** {round(source['score'], 4)}
                        """
                    )

                    st.markdown(
                        "#### Source Content"
                    )

                    st.write(
                        source["content"]
                    )

# ------------------ CHAT INPUT ------------------

question = st.chat_input(
    "Ask a question from the PDF..."
)

# ------------------ HANDLE QUESTION ------------------

if question:

    # ---------- CHECK PDF ----------

    if (
        st.session_state.vectorstore
        is None
    ):

        st.warning(
            "Please upload a PDF first."
        )

    else:

        # ---------- USER MESSAGE ----------

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):

            st.markdown(question)

        # ---------- ASSISTANT RESPONSE ----------

        with st.chat_message("assistant"):

            response_container = st.empty()

            with st.spinner("Thinking..."):

                try:

                    response = ask_question(
                        question=question,
                        vectorstore=(
                            st.session_state.vectorstore
                        ),
                        k=3
                    )

                    answer = response["answer"]

                    response_container.markdown(
                        answer
                    )

                    # ---------- SOURCES ----------

                    with st.expander(
                        "View Sources"
                    ):

                        for source in (
                            response["sources"]
                        ):

                            st.markdown(
                                f"""
                                ### 📄 Source

                                **Page:** {source['page']}

                                **Score:** {round(source['score'], 4)}
                                """
                            )

                            st.markdown(
                                "#### Source Content"
                            )

                            st.write(
                                source["content"]
                            )

                    # ---------- SAVE MESSAGE ----------

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": response["sources"]
                    })

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )