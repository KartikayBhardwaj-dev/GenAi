import os

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq

load_dotenv()

# ---------------- LLM ----------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=300,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- PROMPT ----------------

with open(
    "/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week08_project02/backend/prompts/prompt.txt",
    "r"
) as f:

    template = f.read()

prompt = PromptTemplate.from_template(template)

# ---------------- OUTPUT PARSER ----------------

parser = StrOutputParser()

# ---------------- CHAIN ----------------

chain = prompt | llm | parser