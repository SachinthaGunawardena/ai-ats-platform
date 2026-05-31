from docx import Document

def extract_docx_text(file_path):
    doc = Document(file_path)

    return "\n".join(
        para.text for para in doc.paragraphs
    )