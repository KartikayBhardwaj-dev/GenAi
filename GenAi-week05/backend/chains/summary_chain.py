import os
import time
import logging
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# ------------------ LOGGING ------------------
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/extraction_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# --------------MODEL-------------------------------
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    provider="groq",
    temperature=0.2,
    max_new_tokens=200,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

# ----------------PROMPT-----------------------------
file_path = "/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week05/backend/prompts/summary_prompt.txt"

with open(file_path, "r") as f:
    template = f.read()

prompt = PromptTemplate.from_template(template)

# ------------------ CLEANER ------------------
def clean_summary(text: str) -> str:
    if hasattr(text, "content"):
        text = text.content

    # remove thinking traces
    if "<think>" in text:
        text = text.split("</think>")[-1]

    # remove markdown (``` blocks)
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            if "-" in part:
                text = part
                break

    return text.strip()

cleaner = RunnableLambda(clean_summary)

# -----------------CHAIN--------------------------

summary_chain = prompt | model | cleaner

# text = """

# Rahul Sharma is a Backend Developer with around 2 years of experience.

# He has worked extensively with Python, FastAPI, and MongoDB.

# He has built REST APIs and handled backend system design.

# Projects:

# - Developed scalable API services using FastAPI

# - Designed database schemas using MongoDB

# - Worked on deployment using Docker

# He has experience working in agile teams and building production-ready systems.

# """

# result = chain.invoke({"input": text})

# print(result)