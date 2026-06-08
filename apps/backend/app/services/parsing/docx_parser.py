from docx import Document


def extract_text_from_docx(file_path: str):

    doc = Document(file_path)

    return "\n".join(
        [paragraph.text for paragraph in doc.paragraphs]
    )