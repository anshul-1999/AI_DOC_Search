
AI Document Search & Chat (Hybrid RAG System)

A Retrieval-Augmented Generation (RAG) system that allows users to upload PDFs and chat with them using hybrid search (BM25 + embeddings) and a local LLM via Ollama.

Features:
- PDF upload and processing
- Hybrid search (BM25 + FAISS embeddings)
- Chat memory (multi-turn conversations)
- Local LLM (Ollama)
- Source-grounded answers

Tech Stack:
Python, FastAPI, Streamlit, FAISS, SentenceTransformers, rank-bm25, PyMuPDF, Ollama

How it works:
User -> Streamlit -> FastAPI -> RAG pipeline -> LLM -> Response

Setup:
1. Install dependencies
2. Run Ollama (mistral or llama3)
3. Start FastAPI backend
4. Start Streamlit frontend

Usage:
Upload a PDF and ask questions like:
- Summarize this document
- What are the key findings?
- Explain section 2

<img width="1920" height="1080" alt="Screenshot (152)" src="https://github.com/user-attachments/assets/b99a99d9-8225-4a95-b3fe-9cecb6a22437" />

<img width="1920" height="1080" alt="Screenshot (153)" src="https://github.com/user-attachments/assets/0795914a-d18b-4b61-8903-5a57464c80e9" />

<img width="1920" height="1080" alt="Screenshot (154)" src="https://github.com/user-attachments/assets/8f85abf1-e6ed-4559-a929-c3a5d1f3fecf" />
