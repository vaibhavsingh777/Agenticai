import wikipedia
from graph.state import TutorState

def wiki_research_node(state: TutorState):
    """
    AGENT 4: The Wikipedia Fetcher.
    Responsibility: Pull external web context for the Master Teacher.
    """
    query = state["current_answer"]
    
    try:
        # Search Wikipedia and grab a 3-sentence summary
        search_results = wikipedia.search(query)
        if search_results:
            wiki_summary = wikipedia.summary(search_results[0], sentences=3)
            context = f"Wikipedia says: {wiki_summary}"
        else:
            context = "No relevant Wikipedia articles found."
    except Exception as e:
        context = "Wikipedia search failed or returned ambiguous results."
        
    return {"wiki_context": context}