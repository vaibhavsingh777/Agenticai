# scripts/debug_retrieval2.py
from retriever.vector_store import load_vector_store

vs = load_vector_store()
for q in ["conditional probability definition", "independent events probability"]:
    print(f"=== Query: {q} ===")
    docs = vs.similarity_search(q, k=3)
    for d in docs:
        print(d.page_content[:200])
        print("---")
    print()