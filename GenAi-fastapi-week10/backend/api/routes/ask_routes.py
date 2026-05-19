from fastapi import (APIRouter, HTTPException)
from backend.api.schemas.request_schema import (AskRequest)
from backend.api.schemas.response_schema import (
    AskResponse
)
from backend.pipeline.conversational_pipeline import (ask_question)
router = APIRouter()

# -----------ASK QUESTION-------
@router.post("/ask", response_model=AskResponse)
async def ask_pdf(request: AskRequest):
    try:
        # ---------VALIDATE QUESTION--------
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # -------ASK PIPELINE--------
        response = ask_question(question=request.question, session_id=request.session_id)
         # ---------- SESSION VALIDATION ----------

        if "error" in response:

            raise HTTPException(

                status_code=404,

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