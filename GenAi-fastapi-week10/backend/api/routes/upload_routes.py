import os 
import uuid
from fastapi import (APIRouter, UploadFile, File, Form, HTTPException)
from backend.pipeline.conversational_pipeline import (build_vectorstore)

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
ALLOWED_EXTENSIONS = [".pdf"]
# --------UPLOAD PDF--------
@router.post("/upload")
async def upload_pdf(session_id: str = Form(...), file: UploadFile = File(...)):
    try:
        # -------VALIDATE FILE TYPE------
        filename = file.filename
        extensions = os.path.splitext(filename)[1].lower()
        if extensions not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Only PDF file allowed")
        
        # --------CREATE UNIQUE FILENAME
        unique_filename = (f"{uuid.uuid4()}_{file.filename}"

        )

        file_path = os.path.join(

            UPLOAD_DIR,

            unique_filename

        )
        # ------SAVE FILE------
        with open(file_path, "wb") as f:
            contents = await file.read()
            f.write(contents)

        print("\n========== PDF SAVED ==========")

        print(file_path)

        # ---------- BUILD VECTORSTORE ----------

        print("\n========== PROCESSING PDF ==========")

        build_vectorstore(
            pdf_path=file_path,
            session_id=session_id

        )

        print("\n========== SESSION READY ==========")

        # ---------- RESPONSE ----------

        return {

            "status": "success",

            "message":

            "PDF uploaded and processed successfully.",

            "session_id":

            session_id,

            "filename":

            filename

        }

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )