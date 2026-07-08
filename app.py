import re
import streamlit as st
from graph.workflow import run_multi_agent

st.set_page_config(page_title="Socratic Feynman Tutor", page_icon="🎓")
st.title("🎓 Multi-Agent Socratic Tutor")
st.markdown("I will not give you the answers. I will force you to explain them.")

# Initialize session state for the LangGraph
if "graph_state" not in st.session_state:
    st.session_state.graph_state = {"messages": []}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for role, text in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(text)

# Chat input
if query := st.chat_input("Explain a concept or ask a question..."):
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.chat_history.append(("user", query))
    
    # Run graph using the new modular workflow
    with st.spinner("Agents are collaborating on your input..."):
        response, new_state = run_multi_agent(query, st.session_state.graph_state)
        st.session_state.graph_state = new_state
        
    with st.chat_message("assistant"):
        st.markdown(response)
        
        # Render Math blocks
        latex_blocks = re.findall(r"\$\$(.*?)\$\$", response, re.DOTALL)
        for expr in latex_blocks:
            st.latex(expr.strip())
            
    st.session_state.chat_history.append(("assistant", response))