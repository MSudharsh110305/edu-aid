from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text
    except Exception as e:
        return f"Error: {str(e)}"
