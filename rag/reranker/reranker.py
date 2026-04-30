from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(self):
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rerank(self, query, docs):
        pairs = [[query, d["text"]] for d in docs]
        scores = self.model.predict(pairs)

        ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
        return [r[0] for r in ranked]