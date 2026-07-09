# scripts/debug_retrieval.py
from retriever.vector_store import load_vector_store

vs = load_vector_store()
query = "A random variable is a function that maps outcomes in a sample space to real numbers"
docs = vs.similarity_search(query, k=2)
for i, d in enumerate(docs):
    print(f"--- Retrieved chunk {i+1} ---")
    print(d.page_content)
    print()