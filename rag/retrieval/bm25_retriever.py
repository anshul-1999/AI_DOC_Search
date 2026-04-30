from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self):
        self.docs = []
        self.tokenized_docs = []
        self.bm25 = None

    def build(self, docs):
        self.docs = docs
        self.tokenized_docs = [d["text"].split() for d in docs]
        self.bm25 = BM25Okapi(self.tokenized_docs)

    def search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())

        ranked = sorted(
            zip(self.docs, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [doc for doc, _ in ranked[:k]]