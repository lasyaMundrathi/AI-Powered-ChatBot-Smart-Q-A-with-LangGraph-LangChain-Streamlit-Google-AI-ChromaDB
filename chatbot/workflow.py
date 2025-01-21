from langgraph.graph import StateGraph, START, END
from typing import List
from typing_extensions import TypedDict
from .retrieval import retrieve
from .grading import grade_documents
from .generation import generate
from .query_transformation import transform_query
from .web_search import web_search

class State(TypedDict):
    question: str
    generation: str
    web_search: str
    documents: List[Document]

def build_workflow(chatbot):
    """Build the chatbot workflow."""
    workflow = StateGraph(State)
    workflow.add_node("retrieve", lambda s: retrieve(chatbot, s))
    workflow.add_node("grade_documents", lambda s: grade_documents(chatbot, s))
    workflow.add_node("generate", lambda s: generate(chatbot, s))
    workflow.add_node("transform_query", lambda s: transform_query(chatbot, s))
    workflow.add_node("web_search_node", lambda s: web_search(chatbot, s))

    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "grade_documents")
    workflow.add_edge("grade_documents", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()
