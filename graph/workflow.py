from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from graph.state import TutorState

# Import all 5 agents!
from agents.critic.feynman_analyst import feynman_analyst_node
from agents.guide.socratic_guide import socratic_guide_node
from agents.router.intent_router import intent_router_node
from agents.researcher.wiki_agent import wiki_research_node
from agents.guide.teacher_agent import master_teacher_node

def determine_track(state: TutorState):
    """
    SUPERVISOR ROUTER: Decides which multi-agent track to execute.
    """
    intent = state.get("user_intent", "EVALUATE_ME")
    if "TEACH_ME" in intent:
        return "wiki_researcher"
    else:
        return "feynman_analyst"

# Initialize the graph
workflow = StateGraph(TutorState)

# Add all 5 nodes
workflow.add_node("intent_router", intent_router_node)
workflow.add_node("wiki_researcher", wiki_research_node)
workflow.add_node("master_teacher", master_teacher_node)
workflow.add_node("feynman_analyst", feynman_analyst_node)
workflow.add_node("socratic_guide", socratic_guide_node)

# --- THE GRAPH ARCHITECTURE ---

# 1. Every message goes to the Router first
workflow.add_edge(START, "intent_router")

# 2. Router branches into two separate paths
workflow.add_conditional_edges("intent_router", determine_track)

# Path A: The Teacher Track
workflow.add_edge("wiki_researcher", "master_teacher")
workflow.add_edge("master_teacher", END)

# Path B: The Feynman Track
workflow.add_edge("feynman_analyst", "socratic_guide")
workflow.add_edge("socratic_guide", END)

# Compile
multi_agent_app = workflow.compile(debug=True)

def run_multi_agent(user_input: str, current_state: dict):
    if current_state is None:
        current_state = {"messages": []}
        
    current_state["messages"].append(HumanMessage(content=user_input))
    current_state["current_answer"] = user_input
    
    print(f"\n🚀 Processing: {user_input}")
    
    final_state = multi_agent_app.invoke(current_state)
    
    return final_state["messages"][-1].content, final_state