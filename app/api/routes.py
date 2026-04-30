from fastapi import APIRouter, UploadFile
import os

from app.services.rag_service import RAGService
from rag.ingestion.pdf_loader import extract_text_from_pdf
from rag.ingestion.chunker import chunk_text

router = APIRouter()
rag = RAGService()

@router.post("/upload")
async def upload(file: UploadFile):
    os.makedirs("data", exist_ok=True)

    path = f"data/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)

    rag.build_index(chunks)

    return {"message": "PDF indexed successfully"}

@router.get("/query")
async def query(q: str):
    answer, sources = rag.query(q)

    return {
        "answer": answer,
        "sources": sources
    }