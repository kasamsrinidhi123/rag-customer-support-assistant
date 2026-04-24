# app.py

import streamlit as st
from langgraph_pipeline import run_langgraph

st.title("🤖 RAG Customer Support Assistant (LangGraph + HITL)")

query = st.text_input("Ask your question:")

if st.button("Submit"):
    if query:
        with st.spinner("Processing..."):
            answer = run_langgraph(query)

        st.success(answer)   # ✅ better UI