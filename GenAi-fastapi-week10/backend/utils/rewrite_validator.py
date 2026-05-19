from backend.chains.rag_chain import llm

VALIDATION_PROMPT = """
You are a validator.

Your job is to determine whether the rewritten question
preserves the SAME meaning as the original question.

RULES:

- The rewritten question must NOT introduce:
  - new locations
  - new people
  - new concepts
  - new assumptions

- The rewritten question should ONLY:
  - resolve pronouns
  - clarify references

Return ONLY:

VALID

or

INVALID

------------------------

ORIGINAL QUESTION:
{original_question}

------------------------

REWRITTEN QUESTION:
{rewritten_question}

------------------------

RESULT:
"""

def validate_rewrite(
    original_question,
    rewritten_question
):

    response = llm.invoke(

        VALIDATION_PROMPT.format(

            original_question=original_question,

            rewritten_question=rewritten_question
        )
    )

    result = response.content.strip().upper()

    return result == "VALID"