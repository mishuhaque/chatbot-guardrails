from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    """
    Retrieves supporting documents using FAISS vector search (RAG).
    """

    def __init__(self, docs=None, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

        # Default knowledge base (can be replaced by external corp data)
        self.docs = docs or [
            "DeepSeek was released in 2023 by DeepSeek AI.",
            "ChatGPT is developed by OpenAI.",
            "FastAPI is a modern, fast Python web framework for APIs."
        ]

        # Build embeddings + FAISS index
        embeddings = self.model.encode(self.docs)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def retrieve(self, query: str, top_k: int = 2) -> list:
        """
        Return top_k most relevant docs for the query.
        """
        query_emb = self.model.encode([query])
        D, I = self.index.search(np.array(query_emb), top_k)
        return [self.docs[i] for i in I[0]]
