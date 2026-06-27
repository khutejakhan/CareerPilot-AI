import streamlit as st

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

from components.footer import show_footer
from components.sidebar import show_sidebar
from components.hero import show_hero
from components.input_form import show_input_form
from utils.pdf_generator import create_pdf
from components.charts import show_learning_timeline
from utils.roadmap_generator import generate_roadmap


def load_css():

    with open(
        "styles/style.css",
        encoding="utf-8"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

show_sidebar()
show_hero()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Career Paths", "50+")

with col2:
    st.metric("Projects Suggested", "500+")

with col3:
    st.metric("AI Powered", "Gemini 2.5")

skills, role, months, generate = show_input_form()


if generate:

    with st.spinner("🤖 AI is building your career roadmap..."):
        roadmap = generate_roadmap(skills, role, months)

    st.success("Roadmap generated successfully! 🚀")

    st.markdown(roadmap)

    st.markdown("---")
    st.subheader("📈 Your Learning Timeline")

    show_learning_timeline(months)

    # Create PDF
    pdf_path = create_pdf(roadmap)

    # Download button
    with open(pdf_path, "rb") as file:
        st.download_button(
            " Download Roadmap PDF",
            data=file,
            file_name="career_roadmap.pdf",
            mime="application/pdf",
            use_container_width=True
        )

show_footer()