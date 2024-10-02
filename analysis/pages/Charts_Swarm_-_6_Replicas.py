import altair as alt
import pandas as pd
import streamlit as st


st.markdown("# Charts")

st.text("These requests perform a SELECT query on PostgreSQL, validate the email and password (hash), and return a JWT token.")


def page():

    df = pd.read_csv("tests/comparison.csv")
    df = df[df['Requests'].notna()]
    # df = df[df["Postgres"] == True]
    # df = df[df["Instances"].isin(["GCP 1", "GCP 4"])]
    # df = df[df["Instances"] == "GCP 1"]

    df = df[df["Replicas"] == 6]
    df_gcp1 = df[df["Instances"] == "GCP 1"]
    df_gcp4 = df[df["Instances"] == "GCP 4"]

    # Bar chart - Failed Requests

    st.markdown("## Failed Requests")
    st.text("Less is better")
    # st.bar_chart(
    #     data=df, 
    #     x="Test (lang + framework)", 
    #     y="Failed Requests", 
    #     # y=["Failed Requests","Concurrency Level"], 
    #     color="Concurrency Level",
    #     # color=["#FF0000", "#0000FF"],
    #     stack=False,
    #     use_container_width=True
    # )
    st.text("Both have 0 failed requests.")

    # Bar chart - Requests per Second

    st.markdown("## Requests per Second")
    st.text("More is better")

    st.markdown("#### 1 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp1, 
        x="Test (lang + framework)", 
        y="Request per Second", 
        # y=["Request per Second", "Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    st.markdown("#### 4 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp4, 
        x="Test (lang + framework)", 
        y="Request per Second", 
        # y=["Request per Second", "Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    # Bar chart - Time per Request (ms)*

    st.markdown("## Time per Request (ms)*")
    st.text("Less is better")

    st.markdown("#### 1 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp1, 
        x="Test (lang + framework)", 
        y="Time per Request (ms)*", 
        # y=["Concurrency Level", "Time per Request (ms)*"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    st.markdown("#### 4 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp4, 
        x="Test (lang + framework)", 
        y="Time per Request (ms)*", 
        # y=["Concurrency Level", "Time per Request (ms)*"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    st.text("* mean, across all concurrent requests")

    # Bar chart - Transfer Rate (Kbytes/sec)

    st.markdown("## Transfer Rate (Kbytes/sec)")
    st.text("More is better")

    st.markdown("#### 1 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp1, 
        x="Test (lang + framework)", 
        y="Transfer Rate (Kbytes/sec)", 
        # y=["Transfer Rate (Kbytes/sec)","Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    st.markdown("#### 4 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp4, 
        x="Test (lang + framework)", 
        y="Transfer Rate (Kbytes/sec)", 
        # y=["Transfer Rate (Kbytes/sec)","Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    # Bar chart - Total Time Taken (s)

    st.markdown("## Total Time Taken (s)")
    st.text("Less is better")

    st.markdown("#### 1 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp1, 
        x="Test (lang + framework)", 
        y="Total Time Taken (s)", 
        # y=["Total Time Taken (s)","Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    st.markdown("#### 4 Instância Compute Engine")
    st.bar_chart(
        data=df_gcp4, 
        x="Test (lang + framework)", 
        y="Total Time Taken (s)", 
        # y=["Total Time Taken (s)","Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )


page()