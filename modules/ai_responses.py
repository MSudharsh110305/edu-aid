import openai
from modules.web_scraper import scrape_website
from modules.drive_storage import save_text_to_drive

# Set up OpenAI API key
openai.api_key = 'your-api-key'  # Replace with your actual OpenAI API key

def get_ai_response(prompt, tags=[]):
    try:
        formatted_prompt = f"Tags: {', '.join(tags)}\n\n{prompt}"
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=formatted_prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def get_response_from_websites(question, urls):
    combined_content = ""
    for url in urls:
        combined_content += scrape_website(url)
    
    # Save combined content to Google Drive
    save_text_to_drive(combined_content, "combined_content.txt")
    
    prompt = f"Answer the question based on the following information:\n\n{combined_content}\n\nQuestion: {question}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
