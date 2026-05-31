def parse_resume(path):
    if path.endswith(".pdf"):
        return extract_pdf_text(path)

    elif path.endswith(".docx"):
        return extract_docx_text(path)

    raise Exception("Unsupported file")
