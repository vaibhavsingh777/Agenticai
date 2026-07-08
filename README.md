# 🤖 LLM Chat Tutor Agent

Here I have tried to solve a simple probelm of making a **conversational AI tutor** powered by **LLaMA 3** (via [Ollama](https://ollama.com)) that can:

- ✅ Answer questions from **PDF course books** (RAG) . You as a tutor or student can upload study material from your course content for example CS771 for passing your midsems :P !
- 🌐 Retrieve information from the **web** (DuckDuckGo) . Duh its needed if you wanna score above avg.
- 📖 Pull facts from **Wikipedia**. Because one can never forget the OG wikipedia
- 🧮 Perform **Python calculations and code execution** . Needed for actual coding probelms ( trust me you will get most of these in IITK courses)
- 🧠 Maintain **chat history and context** . Because a tutor learns your ways and history :) like most IIT Kanpur Profs!
- 🧾 **Formatted equation rendering** using **LaTeX** 
- A clean and interactive **Streamlit app interface**

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

---

## 📁 Directory Structure
```
ollama_chat-tutor-agent_project/
├── agents/
│ └── chat_agent.py # Main conversational agent setup
├── data/
│ ├── raw_pdfs/ # PDF books or materials
│ └── db/ # FAISS vector store (auto-created)
├── retriever/
│ ├── vector_store.py # FAISS-based PDF retriever
│ └── web_retrievers.py # Web + Wikipedia retrievers
├── scripts/
│ ├── index_data.py # Index PDF content into vector store
│ └── chat_loop.py # CLI chatbot loop
├── app.py # 🔥 Streamlit UI app
├── requirements.txt # Python dependencies
└── README.md # This file
```
## Project Architecture
```
        ┌────────────┐
        │ User Input │
        └─────┬──────┘
              │
              ▼
     ┌────────────────────---------------------------┐
     │  Conversational Agent (LLaMA3.2)              │
     └────┬─────────────┬────--──────----------------┘
          │             │             │             │
          ▼             ▼             ▼             ▼
 ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
 │ PDF Search  │ │ Web Search  │ │ Wikipedia   │ │ Python REPL  │
 │ (FAISS RAG) │ │ (DuckDuckGo)│ │ Retriever   │ │   Code Exec. │
 └─────────────┘ └─────────────┘ └─────────────┘ └──────────────┘
          │             │                 │           │
          └─────────────┴─────────────────┴───────────┘
                        │
                        ▼
              ┌────────────────────┐
              │ Generated Response │
              └────────────────────┘

```
---

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
