import streamlit as st


def show_input_form():

    st.subheader("🎯 Build Your Career Roadmap")

    col1, col2 = st.columns(2)

    with col1:
        current_skills = st.multiselect(
            "Current Skills",
            [
                "Python",
                "SQL",
                "Machine Learning",
                "HTML",
                "CSS",
                "JavaScript",
                "Data Structures",
                "Git"
            ]
        )

    with col2:
        dream_role = st.selectbox(
            "Desired Career",
            [
                "AI Engineer",
                "Data Scientist",
                "ML Engineer",
                "Full Stack Developer",
                "Cloud Engineer"
            ]
        )

    months = st.slider(
        "Learning Timeline (Months)",
        3,
        12,
        6
    )

    generate = st.button(
        "🚀 Generate AI Roadmap",
        use_container_width=True
    )

    return current_skills, dream_role, months, generate