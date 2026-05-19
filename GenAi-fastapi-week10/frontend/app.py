import streamlit as st
import requests
import uuid

# ---------- PAGE CONFIG ----------

st.set_page_config(
    page_title="AI PDF Chat",
    page_icon="📄",
    layout="wide"
)

# ---------- API URL ----------

API_URL = "http://127.0.0.1:8000"

# ---------- SESSION STATE ----------

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False

# ---------- TITLE ----------

st.title("📄 AI PDF Chat Application")

st.markdown(
    "Upload a PDF and chat with it using Conversational RAG."
)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    # ---------- UPLOAD BUTTON ----------

    if st.button("Upload PDF"):

        if uploaded_file is None:

            st.error(
                "Please select a PDF file."
            )

        else:

            try:

                # ---------- FILES ----------

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        "application/pdf"
                    )
                }

                # ---------- FORM DATA ----------

                data = {
                    "session_id":
                    st.session_state.session_id
                }

                # ---------- API CALL ----------

                with st.spinner(
                    "Processing PDF..."
                ):

                    response = requests.post(
                        f"{API_URL}/upload",
                        files=files,
                        data=data
                    )

                # ---------- SUCCESS ----------

                if response.status_code == 200:

                    st.session_state.pdf_uploaded = True

                    st.success(
                        "PDF uploaded successfully."
                    )

                # ---------- FAILURE ----------

                else:

                    st.error(
                        response.json().get(
                            "detail",
                            "Upload failed"
                        )
                    )

            except Exception as e:

                st.error(str(e))

    # ---------- SESSION INFO ----------

    st.divider()

    st.markdown("### Session ID")

    st.code(
        st.session_state.session_id
    )

# ---------- MAIN CHAT UI ----------

st.subheader("Chat With PDF")

# ---------- DISPLAY CHAT HISTORY ----------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# ---------- CHAT INPUT ----------

question = st.chat_input(
    "Ask a question about the PDF..."
)

# ---------- ASK QUESTION ----------

if question:

    # ---------- CHECK PDF ----------

    if not st.session_state.pdf_uploaded:

        st.warning(
            "Please upload a PDF first."
        )

    else:

        # ---------- ADD USER MESSAGE ----------

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        # ---------- DISPLAY USER ----------

        with st.chat_message("user"):

            st.markdown(question)

        try:

            payload = {
                "question": question,
                "session_id":
                st.session_state.session_id
            }

            # ---------- API CALL ----------

            with st.spinner(
                "Generating answer..."
            ):

                response = requests.post(
                    f"{API_URL}/chat",
                    json=payload
                )

            # ---------- RESPONSE ----------

            if response.status_code == 200:

                data = response.json()

                answer = data.get(
                    "answer",
                    "No answer generated."
                )

                sources = data.get(
                    "sources",
                    []
                )

                # ---------- DISPLAY AI ----------

                with st.chat_message(
                    "assistant"
                ):

                    st.markdown(answer)

                    # ---------- SOURCES ----------

                    if sources:

                        with st.expander(
                            "View Sources"
                        ):

                            for i, source in enumerate(
                                sources
                            ):

                                st.markdown(
                                    f"""
### Source {i+1}

**Page:** {source.get("page")}

**Score:** {round(source.get("score", 0), 4)}

```text
{source.get("content")}
```
"""
                                )

                # ---------- SAVE AI MESSAGE ----------

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            else:

                st.error(
                    response.json().get(
                        "detail",
                        "Chat request failed."
                    )
                )

        except Exception as e:

            st.error(str(e))