import os
import google.generativeai as genai

from dotenv import load_dotenv
from utils.prompts import build_prompt


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_roadmap(skills, role, months):

    prompt = build_prompt(
        skills,
        role,
        months
    )

    response = model.generate_content(prompt)

    return response.text