from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from retriever.vector_store import load_vector_store
from graph.state import TutorState

llm = ChatOllama(model="llama3.2")
vector_store = load_vector_store()

def master_teacher_node(state: TutorState):
    """
    AGENT 5: The Step-by-Step Teacher.
    Responsibility: Teach the student a concept using Wikipedia + PDF context.
    """
    query = state["current_answer"]
    wiki_context = state.get("wiki_context", "")
    
    # Grab PDF context
    docs = vector_store.similarity_search(query, k=2)
    pdf_context = "\n".join([doc.page_content for doc in docs])
    
    sys_prompt = f"""You are a Master AI Teacher. 
    The student has asked you to explain a concept. Do not ask Socratic questions right now; teach them step-by-step.
    
    Use this information from their Course Textbook (Highest Priority):
    {pdf_context}
    
    Use this information from Wikipedia (Secondary Context):
    {wiki_context}
    
    Explain the concept clearly, use bullet points if helpful, and render any math in LaTeX block format ($$).
    """
    
    messages = [SystemMessage(content=sys_prompt)] + state["messages"]
    response = llm.invoke(messages)
    
    return {"messages": [response]}