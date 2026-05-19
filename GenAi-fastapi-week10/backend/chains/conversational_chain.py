from langchain_core.prompts import (PromptTemplate)
from langchain_core.output_parsers import (StrOutputParser)
from backend.chains.rag_chain import (llm)

# -------LOAD PROMPT--------
with open("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-fastapi-week10/backend/prompts/chat_prompt.txt", "r") as f:
    template = f.read()

prompt = PromptTemplate.from_template(template)

# ---------OUTPUT PARSERS---------
parser = StrOutputParser()

# ------------CONVERSATION CHAIN-------
conversational_chain = (
    prompt
    | llm
    | parser
)