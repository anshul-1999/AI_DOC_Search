from rag.embedding.embedder import Embedder
from rag.retrieval.vector_store import VectorStore
from rag.retrieval.bm25_retriever import BM25Retriever
from rag.reranker.reranker import Reranker
from rag.generation.generator import generate_answer

class RAGService:
    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = None
        self.bm25 = BM25Retriever()
        self.reranker = Reranker()

        # 🧠 MEMORY ADDED
        self.chat_history = []

    def update_memory(self, role, message):
        self.chat_history.append({
            "role": role,
            "content": message
        })
        self.chat_history = self.chat_history[-10:]  # keep last 10

    def build_index(self, chunks):
        texts = [c["text"] for c in chunks]

        embeddings = self.embedder.embed(texts)

        self.vector_store = VectorStore(len(embeddings[0]))
        self.vector_store.add(embeddings, chunks)

        self.bm25.build(chunks)

    def hybrid_search(self, query, k=10):
        query_emb = self.embedder.embed([query])[0]

        semantic = self.vector_store.search(query_emb, k)
        keyword = self.bm25.search(query, k)

        combined = semantic + keyword

        seen = set()
        results = []

        for d in combined:
            if d["text"] not in seen:
                seen.add(d["text"])
                results.append(d)

        return results

    def query(self, query):
        # 1. retrieve
        retrieved = self.hybrid_search(query, k=10)
        top_docs = retrieved[:3]

        # 2. build history string
        history_text = "\n".join([
            f"{m['role']}: {m['content']}"
            for m in self.chat_history
        ])

        # 3. generate answer
        answer = generate_answer(query, top_docs, history_text)

        # 4. store memory
        self.update_memory("user", query)
        self.update_memory("assistant", answer)

        return answer, top_docs