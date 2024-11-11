import openai
import pytesseract
from PIL import Image
from pdfminer.high_level import extract_text

# Set up OpenAI API key
openai.api_key = 'your-api-key'  # Replace with your actual OpenAI API key

# Function to get AI-generated response based on prompt and tags
def get_ai_response(prompt, tags=[]):
    try:
        # Combine tags and prompt for context
        formatted_prompt = f"Tags: {', '.join(tags)}\n\n{prompt}"
        response = openai.Completion.create(
            engine="text-davinci-003",  # or use GPT-4 if available
            prompt=formatted_prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to perform OCR on an uploaded image
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    try:
        extracted_text = extract_text(pdf_path)
        return extracted_text
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage of each feature:

# 1. Prompt-based AI Response
prompt = "What are some innovative project ideas in machine learning?"
tags = ["Machine Learning", "Data Science"]
print("AI Response:", get_ai_response(prompt, tags))

# 2. OCR from Image
# Replace 'path/to/image.jpg' with actual path of your image file
image_path = 'path/to/image.jpg'
print("Extracted Text from Image:", extract_text_from_image(image_path))

# 3. Text Extraction from PDF
# Replace 'path/to/document.pdf' with actual path of your PDF file
pdf_path = 'path/to/document.pdf'
print("Extracted Text from PDF:", extract_text_from_pdf(pdf_path))
