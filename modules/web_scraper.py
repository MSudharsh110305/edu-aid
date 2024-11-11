import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])
        return text_content
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
