import streamlit as st
import pandas as pd
import plotly.express as px


def show_learning_timeline(months):

    df = pd.DataFrame({
        "Month": list(range(1, months + 1)),
        "Progress": [
            (i / months) * 100
            for i in range(1, months + 1)
        ]
    })

    fig = px.line(
        df,
        x="Month",
        y="Progress",
        markers=True,
        title="Learning Progress Timeline"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )