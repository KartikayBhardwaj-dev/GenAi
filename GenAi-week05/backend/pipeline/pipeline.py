from backend.utils.pdf_loader import extract_text_from_pdf
from backend.chains.extract_chain import run_with_retry
from backend.chains.extract_chain import extract_chain
from backend.chains.summary_chain import summary_chain
import logging

def run_pipeline(file_path):

    try:
        text = extract_text_from_pdf(file_path)
        logging.info(f"PDF Loaded: {file_path}")
        if not text or not text.strip():
            logging.error(f"PDF loading failed due to empty PDF ")
            return {
                "success": False,
                "data": None
            }

        extract_result = run_with_retry(extract_chain, text)
        logging.info(f"Extraction Done")
        if extract_result["success"] == False:
            logging.error(f"Extraction Failed due to {extract_result}")
            return {
                "success": False,
                "data": None
            }

        summary_result = summary_chain.invoke({
            "input": text
        })
        logging.info(f"Summary Generated")

        return {
            "success": True,
            "data": {
                "extracted": extract_result["data"],
                "summary": summary_result
            }
        }
    except Exception as e:
        logging.error(f"PipeLine Failed due to {str(e)}")
        return {
            "success": False,
            "data": None
        }

