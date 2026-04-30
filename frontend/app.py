import streamlit as st
import requests

st.title("📄 AI PDF Chat (Hybrid RAG)")

file = st.file_uploader("Upload PDF")

if file:
    try:
        requests.post(
            "http://127.0.0.1:8000/upload",
            files={"file": file}
        )
        st.success("PDF uploaded & indexed!")
    except:
        st.error("Backend not running")

query = st.text_input("Ask a question")

if query:
    try:
        res = requests.get(
            "http://127.0.0.1:8000/query",
            params={"q": query}
        )

        data = res.json()

        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Sources")
        for s in data["sources"]:
            st.write("-", s["text"][:200])

    except:
        st.error("Backend not reachable")