from pydantic import BaseModel
from typing import List, Dict, Any

# -------ASK RESPONSE--------
class AskResponse(BaseModel):
    question: str
    standalone_question: str
    answer: str
    sources: List[Dict[str, Any]]

# ---------ERROR MESSAGE--------
class ErrorResponse(BaseModel):
    error: str

    