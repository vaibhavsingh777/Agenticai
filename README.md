# 🤖 LLM Chat Tutor Agent

Here I have tried to solve a simple probelm of making a **conversational AI tutor** powered by **LLaMA 3** (via [Ollama](https://ollama.com)) that can:

---

## 🔧 Features
| Feature               | Source                   | Method                             |
|----------------------|--------------------------|------------------------------------|
| Course Q&A           | Local PDF vector search  | FAISS + Sentence Embeddings (RAG) |
| General Info         | DuckDuckGo Web Search    | LangChain Tool                     |
| Factual Queries      | Wikipedia Search         | LangChain Tool                     |
| Math/Programming     | Python Tool              | Python REPL                        |
| Conversational Memory| Chat History             | LangChain Memory                   |
| Math Formatting      | LaTeX                    | Streamlit LaTeX Renderer           |



## 🚀 Getting Started

### 1. Install Dependencies

Make sure you have Python 3.10+ and FAISS-compatible system. And install ollama on your local PC for running LLM llama3.2
Ensure all dependencies are installed
```bash
pip install -r requirements.txt
ollama run llama3.2
```
### 2. Add Pdfs in data/raw_pdfs/ and index them by
```bash
python scripts/index_data.py
```
### 3. Start the agent
```bash
streamlit run app.py
```
```mermaid
graph TD
    %% User Entry
    User((Student)) --> Router[("Agent 1: Intent Router")]
    
    %% Routing Logic
    Router -- "TEACH_ME" --> Researcher["Agent 2: Wiki Researcher"]
    Router -- "EVALUATE_ME" --> Critic["Agent 3: Feynman Critic"]
    
    %% Track A: Teaching
    Researcher --> Teacher["Agent 4: Master Teacher"]
    Teacher --> Output[("Tutor Response")]
    
    %% Track B: Feynman/Socratic
    Critic --> Guide["Agent 5: Socratic Guide"]
    Guide --> Output
    
    %% RAG Context Connection
    DB[("FAISS Vector Store (Textbooks)")] -.-> Critic
    DB -.-> Teacher
    
    %% Style adjustments for clarity
    classDef agent fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef router fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    class Router router;
