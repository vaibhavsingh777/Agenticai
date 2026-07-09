# scripts/peek_particulate.py
from retriever.vector_store import load_vector_store

vs = load_vector_store()
results = vs.similarity_search("particulate processes granulation polymers", k=5)
for i, r in enumerate(results):
    print(f"--- Chunk {i+1} ---")
    print(r.page_content[:300])
    print()