from pdf_loader import extract_text_from_pdf
from parser import ResumeParser

def process_pdf(file_path: str):
    print("STEP 1: Extracting text...")
    text = extract_text_from_pdf(file_path)

    print("TEXT LENGTH:", len(text))

    print("STEP 2: Parsing...")
    parser = ResumeParser()
    result = parser.parse(text)

    print("STEP 3: Done")

    return result


if __name__ == "__main__":
    result = process_pdf("/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week04_project01/data/resume.pdf")
    print(result)