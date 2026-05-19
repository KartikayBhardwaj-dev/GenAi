# ------------IMPORTS-------------------
import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# --------------LLM------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# -----------PROMPTS-------------
with open("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week09-ChatMemory-project03/backend/prompts/chat_prompt.txt", "r") as f:
    template = f.read()
prompt = PromptTemplate.from_template(template)

# -----------OUTPUT PARSERS----------------
parser = StrOutputParser()
# ------------CHAIN---------------
conversational_chain = prompt | llm | parser
