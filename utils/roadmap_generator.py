import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env locally
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Add it to your local .env file or Streamlit secrets."
    )

genai.configure(api_key=api_key)


def generate_roadmap(skills, role, months):

    prompt = f"""
    You are an expert career mentor.

    Create a detailed {months}-month roadmap to become a {role}.

    Current skills:
    {skills}

    Include:

    1. Month-by-month learning plan
    2. Recommended courses
    3. Hands-on projects
    4. Technologies to learn
    5. Interview preparation tips
    6. Portfolio suggestions

    Format the response beautifully in Markdown.
    """

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text