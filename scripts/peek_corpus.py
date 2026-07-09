# scripts/peek_corpus.py
from retriever.vector_store import load_vector_store

vs = load_vector_store()
results = vs.similarity_search("data science", k=5)
for i, r in enumerate(results):
    print(f"--- Chunk {i+1} ---")
    print(r.page_content[:200])
    print()