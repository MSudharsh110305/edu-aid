import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Paths or other constants can go here
DATA_DIR = "data/"
LOGS_DIR = "logs/"
