import streamlit as st
import tempfile
import sys
import os
from dotenv import load_dotenv

# ✅ Load env (VERY IMPORTANT)
load_dotenv()

# ✅ allow importing backend
sys.path.append(os.path.abspath("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week04_project01/backend"))
from main import process_pdf

st.title("Resume Parser (GenAI)")

# 🔍 Debug: check API key
st.write("API Key Loaded:", os.getenv("HUGGINGFACEHUB_API_TOKEN") is not None)

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file is not None:
    if st.button("Parse Resume"):
        try:
            with st.spinner("Processing..."):

                # ✅ Save temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name

                st.write(f"Temp file: {tmp_path}")  # DEBUG

                # ✅ Call backend
                result = process_pdf(tmp_path)

                st.subheader("Output")

                if isinstance(result, dict) and "error" in result:
                    st.error(result["error"])
                else:
                    st.json(result)

        except Exception as e:
            st.error(f"Error: {str(e)}")