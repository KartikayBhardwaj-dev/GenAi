from fastapi import (APIRouter, HTTPException)
from backend.api.schemas.request_schema import (AskRequest)
from backend.api.schemas.response_schema import (AskResponse)
from backend.pipeline.conversational_pipeline import (ask_question)

router = APIRouter()

# ---------- CHAT ROUTER ----------

@router.post("/chat")

async def chat_with_pdf(request: AskRequest):

    try:
        # -------VALIDATE QUESTION------
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # -------RUN CONVERSATIONAL PIPELINE-------
        response = ask_question(question=request.question, session_id=request.session_id)
         # ---------- INVALID SESSION ----------

        if "error" in response:

            raise HTTPException(

                status_code=400,

                detail=response["error"]

            )

        return response

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )