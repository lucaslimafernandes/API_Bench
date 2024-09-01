import streamlit as st
import pandas as pd


df = pd.read_csv("tests/comparison.csv")


def main():

    st.sidebar.markdown("# Table")
    st.markdown("# API Benchmark - Apache AB - Go, Python 🎈")

    st.markdown("A Simple Benchmark using Go, Python, Nginx and Docker.")





if __name__ == "__main__":

    st.set_page_config(
        page_title="API_Bench", page_icon=":chart_with_upwards_trend:"
    )

    main()