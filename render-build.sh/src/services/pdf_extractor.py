import PyPDF2

def extract_text_from_pdf(path):
    text = ''
    with open(path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text