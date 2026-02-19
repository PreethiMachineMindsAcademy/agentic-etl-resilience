import streamlit as st
import json
from agent import agentic_loop

st.title("🤖 Agentic AI for Autonomous ETL Resilience")

with open("logs.json") as f:
    logs=json.load(f)

for log in logs:
    st.subheader(log["pipeline"])
    st.write("Error:",log["error"])

    if st.button(f"Analyze {log['pipeline']}"):
        decision,action=agentic_loop(log)
        st.success("Decision: "+decision)
        st.info("Action: "+action)

