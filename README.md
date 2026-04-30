
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

