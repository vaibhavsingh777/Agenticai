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
    docs = vector_store.similarity_search(student_answer, k=2)
    truth_context = "\n".join([doc.page_content for doc in docs])
    
    prompt = f"""You are a strict technical reviewer in a multi-agent teaching system.
    The student said: "{student_answer}"
    
    Compare what they said against the textbook material:
    "{truth_context}"
    
    RULES:
    1. If the student is just saying hello or asking a basic question, output "PASS".
    2. If the student is explaining a concept, identify ANY missing core concepts, over-simplifications, or factual errors. 
    3. Do NOT give the student the direct answer. Just write a short critique for the Tutor agent to use.
    4. If their explanation is perfectly aligned with the textbook, output exactly "PASS".
    """
    
    response = llm.invoke(prompt)
    return {"analyst_feedback": response.content}