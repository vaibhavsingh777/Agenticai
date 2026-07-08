from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from graph.state import TutorState

# Independent LLM initialization for this specific agent's persona
llm = ChatOllama(model="llama3.2")

def socratic_guide_node(state: TutorState):
    """
    AGENT 2: The Socratic Tutor.
    Responsibility: Interact with the user safely, using feedback from the Analyst.
    """
    feedback = state.get("analyst_feedback", "")
    
    sys_prompt = """You are a Socratic AI Tutor. You NEVER give direct answers. 
    Your goal is to guide the student to the answer using the Feynman technique (forcing them to explain it simply).
    """
    
    # Dynamically inject the Critic's feedback into the Guide's brain
    if feedback and feedback.strip() != "PASS":
        sys_prompt += f"\n\nINTERNAL SYSTEM MEMO - The Gap Analyst reviewed the student's input and provided this critique: {feedback}. \nFormulate a guiding question based on this critique to help the student realize their mistake. Do not mention the Gap Analyst to the user."
    elif feedback.strip() == "PASS":
        sys_prompt += "\n\nThe student answered perfectly (or is just chatting)! Praise them if they explained a concept, and ask what concept they want to tackle next."
        
    # Combine the system persona with the chat history
    messages = [SystemMessage(content=sys_prompt)] + state["messages"]
    
    response = llm.invoke(messages)
    return {"messages": [response]}