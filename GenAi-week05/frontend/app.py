import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tempfile
import os
from backend.pipeline.pipeline import run_pipeline


# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ------------------ TITLE ------------------
st.title("📄 AI Resume Analyzer")
st.markdown("Upload a resume and get structured insights + summary")

# ------------------ FILE UPLOAD ------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF only)",
    type=["pdf"]
)

# ------------------ ANALYZE BUTTON ------------------
if uploaded_file is not None:

    if st.button("Analyze Resume"):

        # Save file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        # ------------------ LOADING ------------------
        with st.spinner("Analyzing resume..."):

            result = run_pipeline(temp_path)

        # Cleanup temp file
        os.remove(temp_path)

        # ------------------ RESULT HANDLING ------------------
        if not result["success"]:
            st.error("❌ Failed to process resume")
            if result.get("error"):
                st.code(result["error"])
            st.stop()

        data = result["data"]

        # ------------------ EXTRACTION ------------------
        extracted = data["extracted"]

        st.subheader("🧾 Extracted Details")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**Name:** {extracted.get('name')}")
            st.markdown(f"**Role:** {extracted.get('role')}")
            st.markdown(f"**Experience:** {extracted.get('experience_years')} years")

        # Tech Stack
        st.markdown("**Tech Stack:**")
        tech_stack = extracted.get("tech_stack", [])

        if tech_stack:
            st.write(", ".join(tech_stack))
        else:
            st.write("No tech stack found")

        # ------------------ SUMMARY ------------------
        st.subheader("📌 Resume Summary")

        summary = data["summary"]

        # Handle ChatMessage vs string
        if hasattr(summary, "content"):
            summary = summary.content

        st.markdown(summary)