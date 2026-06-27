import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🚀 CareerPilot AI")

        st.markdown(
            """
### Features

✅ Personalized roadmaps

✅ Recommended courses

✅ Real-world projects

✅ Timeline visualization

✅ PDF exports

---

### Built With

- Python
- Streamlit
- Gemini AI
- Plotly

---

Made for aspiring AI engineers ❤️
            """
        )