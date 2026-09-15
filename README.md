# 🤖 Document Chatbot using RAG

An AI-powered chatbot that answers questions from uploaded PDF documents using Retrieval-Augmented Generation (RAG).

## 🚀 Features
- Upload any PDF document
- Ask questions in natural language
- AI answers based only on document content
- Chat history maintained
- Clean and simple UI

## 🛠️ Tech Stack
- **Python** — Core language
- **LangChain** — Pipeline connection
- **FAISS** — Vector database for similarity search
- **Groq LLM API** — AI answer generation
- **FastAPI** — Backend API
- **Streamlit** — Frontend UI
- **HuggingFace Embeddings** — Text to vector conversion

## 📁 Project Structure

document-chatbot/
├── ingest.py # PDF loading and FAISS indexing
├── retriever.py # Similarity search from FAISS
├── llm.py # Groq LLM integration
├── main.py # FastAPI server
├── app.py # Streamlit frontend
└── .env # API keys (not uploaded)

## ⚙️ How it Works
1. User uploads a PDF
2. Document is split into chunks
3. Chunks are converted to embeddings and stored in FAISS
4. User asks a question
5. Similar chunks are retrieved
6. Groq LLM generates answer from retrieved chunks

## 🔧 Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
streamlit run app.py
```