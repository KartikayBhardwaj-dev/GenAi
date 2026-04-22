from pypdf import PdfReader
import logging

def extract_text_from_pdf(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)

        logging.info(f"Loading PDF: {file_path}")
        logging.info(f"Total pages: {len(reader.pages)}")

        text = ""

        for i, page in enumerate(reader.pages):
            try:
                page_text = page.extract_text() or ""   
                text += page_text + "\n"

            except Exception as e:
                logging.warning(f"Failed to read page {i}: {str(e)}")
                continue

        cleaned_text = text.strip()

        logging.info(f"Extracted text length: {len(cleaned_text)}")

        return cleaned_text

    except Exception as e:
        logging.error(f"PDF extraction failed: {str(e)}")
        return ""