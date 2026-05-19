import os

from dotenv import load_dotenv

from langchain.memory import ConversationSummaryMemory

from langchain_groq import ChatGroq

load_dotenv()

# ------------------ LLM ------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ------------------ SUMMARY MEMORY ------------------

summary_memory = ConversationSummaryMemory(
    llm=llm,

    memory_key="chat_history",

    return_messages=True
)