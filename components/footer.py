import streamlit as st


def show_footer():

    st.markdown("---")

    st.markdown(
        """
<div style="text-align:center;color:#94A3B8">

Built with ❤️ using Python, Streamlit and Gemini AI

<br>

CareerPilot AI © 2026

</div>
        """,
        unsafe_allow_html=True
    )