#  GenAI Resume Parser (Full Stack)

This project is a production-style GenAI application that extracts structured data from a resume PDF and returns validated JSON output via both CLI and a Streamlit UI.

---

##  Features

- Upload Resume PDF via UI (Streamlit)
- LLM-powered parsing (Llama 3 via Hugging Face + Groq)
- Prompt Engineering with strict JSON format
- Automatic Retry (API errors + Invalid JSON)
- Schema Validation
- Logging (requests, responses, errors)
- Timeout and Error Handling

---

##  How It Works

PDF → Text Extraction → LLM → JSON → Validation → Retry → Final Output

---

##  Project Structure

genai-resume-parser/

- backend/  
  - main.py              # Entry point  
  - llm_wrapper.py       # LLM handling (retry, logging, JSON enforcement)  
  - parser.py            # Parsing logic + retry + feedback loop  
  - validator.py         # Schema validation  
  - pdf_loader.py        # Extract text from PDF  
  - strict_json.txt      # Prompt template  

- frontend/  
  - app.py               # Streamlit UI  

- logs/  
  - llm_output_logs.txt  

- data/  
  - resume.pdf  

- requirements.txt  
- .env  

---

##  Setup Instructions

### 1 Create Virtual Environment

```bash
python3.10 -m venv venv
```

---

### 2 Activate Environment

**Mac/Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

---

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4 Add Hugging Face API Key

Create a `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Get your token from:  
https://huggingface.co/settings/tokens

---

### 5 Add Your Resume

Replace:

```
data/resume.pdf
```

with your own resume file.

---

## Run the Project

### Backend (CLI Test)

```bash
python backend/main.py
```

---

### Frontend (Streamlit UI)

```bash
streamlit run frontend/app.py
```

---

##  UI Features

- Upload PDF  
- Click **Parse Resume**  
- View structured JSON output  
- Error display if parsing fails  

---

## Example Output

```json
{
  "name": "Rahul Sharma",
  "skills": ["Python", "Node.js", "MongoDB"],
  "experience_years": 2
}
```

---

##  Key Learnings

- Controlling LLM outputs
- Handling API failures and retries
- Enforcing strict JSON structure
- Building real-world GenAI pipelines
- Designing backend + frontend GenAI apps

---

##  Known Limitations

- PDF extraction may be messy for complex layouts
- LLM may hallucinate occasionally
- Large PDFs are truncated due to token limits

---

##  Future Improvements

- Add chunking for large documents
- Use embeddings + RAG
- Build FastAPI backend
- Streaming responses
- LangChain structured output parsers

---

##  Tech Stack

- Python  
- LangChain  
- Hugging Face Hub  
- Groq (LLM provider)  
- Streamlit  
- PyPDF  

---

##  Author

Built as part of a structured GenAI engineering journey 
