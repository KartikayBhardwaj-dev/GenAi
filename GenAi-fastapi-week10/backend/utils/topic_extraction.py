from backend.chains.rag_chain import llm

PROMPT = """
Extract the main topic/entity from the user question.

Examples:

Question: What is LangChain?
Topic: LangChain

Question: Explain FastAPI
Topic: FastAPI

Question: Tell me about Docker
Topic: Docker

Return ONLY the topic.

Question:
{question}
"""

def extract_topic(question):

    response = llm.invoke(
        PROMPT.format(
            question=question
        )
    )

    return response.content.strip()