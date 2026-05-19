from langchain_core.prompts import (
    PromptTemplate
)

from backend.chains.rag_chain import (
    llm
)

# ---------- LOAD PROMPT ----------

with open(
    "/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-fastapi-week10/backend/prompts/standalone_question_prompt.txt",
    "r"
) as f:

    template = f.read()

prompt = PromptTemplate.from_template(
    template
)

# ---------- GENERATE ----------

def generate_standalone_question(

    question,

    chat_history,

    current_topic=None
):

    chain = prompt | llm

    standalone_question = chain.invoke({

        "chat_history": chat_history,

        "question": question,

        "current_topic": current_topic
    })

    return standalone_question.content.strip()