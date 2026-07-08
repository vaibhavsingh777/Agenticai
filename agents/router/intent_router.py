from langchain_ollama import ChatOllama
from graph.state import TutorState

llm = ChatOllama(model="llama3.2", temperature=0) # Temp 0 for strict classification

def intent_router_node(state: TutorState):
    """
    AGENT 3: The Front-Door Classifier.
    Responsibility: Route the user to either the Feynman track or the Teaching track.
    """
    user_input = state["current_answer"]
    
    prompt = f"""You are an intent classifier for an AI Tutor.
    The user said: "{user_input}"
    
    If the user is asking a direct question, asking you to explain something, or saying they don't know, output exactly: TEACH_ME
    If the user is stating a fact, explaining a concept themselves, or answering a question, output exactly: EVALUATE_ME
    
    Output nothing else except one of those two words.
    """
    
    response = llm.invoke(prompt)
    intent = response.content.strip().upper()
    
    # Fallback safety
    if "TEACH_ME" not in intent and "EVALUATE_ME" not in intent:
        intent = "EVALUATE_ME" 
        
    return {"user_intent": intent}