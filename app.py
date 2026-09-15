import streamlit as st
import requests

st.set_page_config(page_title="Document Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 Document Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False

with st.sidebar:
    st.header("📄 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
    
    if uploaded_file is not None and not st.session_state.pdf_uploaded:
        with st.spinner("Processing PDF..."):
            files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
            response = requests.post("http://127.0.0.1:8000/upload", files=files)
            if response.status_code == 200:
                st.success("✅ PDF Ready!")
                st.session_state.pdf_uploaded = True
                st.session_state.pdf_name = uploaded_file.name

    if st.session_state.pdf_uploaded:
        st.info(f"📘 Active: {st.session_state.pdf_name}")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.pdf_uploaded = False

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask a question about your document...")

if question:
    with st.chat_message("user"):
        st.write(question)
    st.session_state.chat_history.append({"role": "user", "content": question})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )
            if response.status_code == 200:
                answer = response.json()["answer"]
                st.write(answer)
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
            else:
                st.error("Something went wrong!")