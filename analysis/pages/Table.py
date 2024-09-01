import pandas as pd
import streamlit as st


st.markdown("# Table ")


def page():

    # table

    df = pd.read_csv("tests/comparison.csv")
    df = df[df['Requests'].notna()]

    st.dataframe(df)

    st.text("* mean, across all concurrent requests")
    st.text("** mean")

page()

# eof
