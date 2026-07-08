from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

class TutorState(TypedDict):
    """Shared state passed between all 5 agents."""
    messages: Annotated[list, add_messages]
    current_answer: str
    
    # Existing Feynman Pipeline State
    analyst_feedback: str
    
    # NEW: Router and Teacher State
    user_intent: str
    wiki_context: str