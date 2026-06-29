import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Add it to your local .env file or Streamlit secrets."
    )

# Configure Gemini
genai.configure(api_key=api_key)


def generate_roadmap(skills, role, months):

    prompt = f"""
You are an expert career mentor and senior software engineer.

Create a professional {months}-month roadmap to become a {role}.

Current skills:
{skills}

Include:

# Month-by-Month Learning Plan
Give clear goals for each month.

# Courses
Recommend free and paid resources.

# Projects
Suggest real-world portfolio projects.

# Technologies
Mention frameworks, tools, and platforms.

# Interview Preparation
Explain what to practice.

# Portfolio Tips
Tell the user what to showcase on GitHub and LinkedIn.

Format everything beautifully in Markdown with headings, bullet points, and emojis.
"""

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        if response and response.text:
            return response.text

        return "⚠️ Gemini returned an empty response."

    except Exception as e:
        return f"❌ Ai service Busy! : {str(e)}"