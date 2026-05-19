import os
from dotenv import load_dotenv
from langchain_core.prompts import (PromptTemplate)
from langchain_core.output_parsers import (StrOutputParser)
from langchain_groq import (ChatGroq)
from backend.config import (LLM_MODEL)
load_dotenv()

# --------LLM---------
llm = ChatGroq(
    model=LLM_MODEL,
    temperature=0.2,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# -----------LOAD PROMPTS----------
with open("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-fastapi-week10/backend/prompts/rag_prompt.txt", "r") as f:
    template = f.read()
prompt = PromptTemplate.from_template(
    template
)

# --------OUTPUT PARSER------------
parser = StrOutputParser()

# -----------RAG CHAIN-----------
rag_chain = (
    prompt
    | llm
    | parser
)