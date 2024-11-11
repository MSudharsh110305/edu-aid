from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    try:
        extracted_text = extract_text(pdf_path)
        return extracted_text
    except Exception as e:
        return f"Error: {str(e)}"
