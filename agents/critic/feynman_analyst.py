from langchain_ollama import ChatOllama
from retriever.vector_store import load_vector_store
from graph.state import TutorState

# Load resources once for speed
llm = ChatOllama(model="llama3.2")
vector_store = load_vector_store()

def feynman_analyst_node(state: TutorState):
    """
    AGENT 1: The strict technical reviewer.
    Responsibility: Check student answers against the FAISS database and flag errors.
    """
    student_answer = state["current_answer"]
    
    # RAG lookup against your local PDFs
    docs = vector_store.similarity_search(student_answer, k=4)
    truth_context = "\n".join([doc.page_content for doc in docs])
    
    prompt = f"""You are a strict technical reviewer in a multi-agent teaching system.
The student said: "{student_answer}"

Here is relevant textbook material (may include specific worked examples alongside general definitions):
"{truth_context}"

RULES:
1. If the student is just saying hello or asking a basic question, output "PASS".
2. Judge ONLY whether the student's CORE conceptual understanding is present and correct.
3. IGNORE imperfect phrasing, informal wording, or minor imprecision as long as the essential idea is right. Do not nitpick word choice.
4. Only flag an issue if there is an actual factual error, a genuinely missing core idea (e.g. omitting that expectation is probability-weighted), or a meaningful oversimplification that would mislead the student.
5. Do NOT flag an explanation just because it's phrased more generally, is less formal than the textbook, or doesn't mention the same example/numbers as the retrieved material.
6. When in doubt between PASS and a minor critique, choose PASS — the goal is to catch real misunderstandings, not to demand textbook-perfect phrasing.
7. Do NOT give the student the direct answer. Just write a short critique for the Tutor agent to use.
8. If the student's core understanding is sound, output exactly "PASS".
"""
    
    response = llm.invoke(prompt)
    return {"analyst_feedback": response.content}