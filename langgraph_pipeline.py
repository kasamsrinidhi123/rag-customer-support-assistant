# langgraph_pipeline.py

from langgraph.graph import StateGraph
from typing import TypedDict
from rag_pipeline import retrieve_docs


# -------------------------------
# STATE
# -------------------------------
class State(TypedDict):
    query: str
    context: str
    answer: str


# -------------------------------
# NODE 1: RETRIEVE
# -------------------------------
def retrieve(state: State):
    query = state["query"]

    context = retrieve_docs(query)

    return {
        "query": query,
        "context": context,
        "answer": ""
    }


# -------------------------------
# NODE 2: GENERATE (UPDATED FORMAT)
# -------------------------------
def generate(state: State):
    context = state["context"]

    # HITL condition
    if not context:
        answer = """
⚠️ We couldn’t find a confident answer.

👨‍💼 Escalated to Human Support.
📧 Our team will contact you shortly.
"""
    else:
        # ✅ FORMATTED ANSWER (IMPORTANT)
        answer = f"""
### ✅ Answer

{context}

---
💬 Need more help? Ask another question.
"""

    return {
        "query": state["query"],
        "context": context,
        "answer": answer
    }


# -------------------------------
# GRAPH BUILD
# -------------------------------
graph = StateGraph(State)

graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)

graph.set_entry_point("retrieve")

graph.add_edge("retrieve", "generate")

app_graph = graph.compile()


# -------------------------------
# RUN FUNCTION
# -------------------------------
def run_langgraph(query: str):
    result = app_graph.invoke({"query": query})
    return result["answer"]