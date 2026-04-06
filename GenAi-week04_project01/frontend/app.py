import streamlit as st
import tempfile
import sys
import os 

#allow importing backend
sys.path.append(os.path.abspath("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week04_project01/backend"))
from main import process_pdf

st.title("Resume parser (GenAi)")
uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file is not None:
    if st.button("Parse Resume"):
        with st.spinner("Processing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name
            result = process_pdf(tmp_path)
            st.subheader("Output")

            if isinstance(result, dict) and "error" in result:
                st.error(result["error"])
            else:
                st.json(result)