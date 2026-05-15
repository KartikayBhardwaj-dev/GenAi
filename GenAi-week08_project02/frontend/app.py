import sys
import os

# ------------------ PATH SETUP ------------------

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# ------------------ IMPORTS ------------------

import tempfile
import streamlit as st

from backend.pipeline.pipeline import (
    build_vectorstore,
    ask_question
)

# ------------------ PAGE CONFIG ------------------

st.set_page_config(
    page_title="PDF QA System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Chat With Your PDF")

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

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_file.read())

        temp_path = temp_file.name

    with st.spinner("Processing PDF..."):

        st.session_state.vectorstore = build_vectorstore(
            pdf_path=temp_path
        )

    st.success("PDF Processed Successfully ✅")

# ------------------ DISPLAY CHAT ------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # ---------- SHOW SOURCES ----------

        if message["role"] == "assistant":

            if "sources" in message:

                with st.expander("Source"):

                    for source in message["sources"]:

                        st.write(f"Page: {source['page']}")

                        st.write(f"Score: {source['score']}")

                        st.markdown("### Source Content")

                        st.write(source["content"])

# ------------------ CHAT INPUT ------------------

question = st.chat_input(
    "Ask question from PDF..."
)

# ------------------ HANDLE QUESTION ------------------

if question:

    if st.session_state.vectorstore is None:

        st.warning("Please upload a PDF first.")

    else:

        # ---------- SAVE USER MESSAGE ----------

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        # ---------- DISPLAY USER MESSAGE ----------

        with st.chat_message("user"):

            st.markdown(question)

        # ---------- GENERATE RESPONSE ----------

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = ask_question(
                    question=question,
                    vectorstore=st.session_state.vectorstore,
                    k=3
                )

                answer = response["answer"]

                st.markdown(answer)

                # ---------- DISPLAY SOURCE ----------

                with st.expander("Source"):

                    for source in response["sources"]:

                        st.write(f"Page: {source['page']}")

                        st.write(f"Score: {source['score']}")

                        st.markdown("### Source Content")

                        st.write(source["content"])

        # ---------- SAVE ASSISTANT MESSAGE ----------

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": response["sources"]
        })