import pandas as pd
import streamlit as st

# import plotly.express as px


st.markdown("# Charts")

# head
# Test (lang + framework),Requests,Concurrency Level,Request per Second,Time per Request (ms)*,Failed Requests,Transfer Rate (Kbytes/sec),Total Time Taken (s),Document Lenght (bytes),Connection Total Times (ms),Connect Time (ms)**,Processing Time (ms)**,Waiting Time (ms)**,Percentile 50% (ms),Percentile 80% (ms),Percentile 100%  (ms)


def page():

    df = pd.read_csv("tests/comparison.csv")
    df = df[df['Requests'].notna()]

    # Bar chart - Failed Requests

    st.markdown("## Failed Requests")
    st.bar_chart(
        data=df, 
        x="Test (lang + framework)", 
        y="Failed Requests", 
        # y=["Failed Requests","Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )

    # Bar chart - Requests per Second

    st.markdown("## Requests per Second")
    st.bar_chart(
        data=df, 
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
    st.bar_chart(
        data=df, 
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
    st.bar_chart(
        data=df, 
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
    st.bar_chart(
        data=df, 
        x="Test (lang + framework)", 
        y="Total Time Taken (s)", 
        # y=["Total Time Taken (s)","Concurrency Level"], 
        color="Concurrency Level",
        # color=["#FF0000", "#0000FF"],
        stack=False,
        use_container_width=True
    )


page()