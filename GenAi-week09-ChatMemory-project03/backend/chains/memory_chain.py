import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
load_dotenv()

# llm
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# CHAT PROMPT
prompt = ChatPromptTemplate.from_messages([

    (

        "system",

        """

You are a helpful AI assistant.

Answer ONLY from the provided context.

If answer is not available,

say:

"I don't know based on the provided document."

Chat History:

{chat_history}

Context:

{context}

"""

    ),

    (

        "human",

        "{question}"

    )

])

# OUTPUT PARSER
parser = StrOutputParser()
# memory chain
memory_chain = prompt | llm | parser