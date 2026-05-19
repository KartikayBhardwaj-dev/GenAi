from pydantic import BaseModel
# ----------ASK REQUEST-------
class AskRequest(BaseModel):
    session_id: str
    question: str

# ------CHAT REQUEST--------
class chatRequest(BaseModel):
    session_id: str
    message: str
    