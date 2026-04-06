from pdf_loader import extract_text_from_pdf
from parser import ResumeParser

def process_pdf(file_path: str):
    text = extract_text_from_pdf(file_path)

    parser = ResumeParser()
    result = parser.parse(text)

    return result


if __name__ == "__main__":
    result = process_pdf("data/resume.pdf")
    print(result)