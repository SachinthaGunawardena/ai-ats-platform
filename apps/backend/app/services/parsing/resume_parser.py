from app.services.parsing.pdf_parser import extract_text_from_pdf
from app.services.parsing.docx_parser import extract_text_from_docx


def extract_text_from_resume(file_path: str, filename: str):

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    if filename.endswith(".docx"):
        return extract_text_from_docx(file_path)

    return ""