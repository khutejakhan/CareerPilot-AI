import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load local .env when running on your computer
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Add it to your local .env file or Streamlit secrets."
    )

genai.configure(api_key=api_key)
## THIS IS ANOTHER ONE 
