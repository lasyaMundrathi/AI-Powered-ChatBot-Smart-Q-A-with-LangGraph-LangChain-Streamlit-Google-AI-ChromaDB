from langgraph.graph import StateGraph, START, END
from typing import List
from typing_extensions import TypedDict
from .retrieval import retrieve
from langchain.schema import Document
from .grading import grade_documents
from .generation import generate
from .query_transformation import transform_query
from .web_search import web_search


# Define the state structure
class State(TypedDict):
    question: str
    generation: str
    web_search: str
    documents: List[Document]

# Decision node function
def decide_to_generate(state: State) -> str:
    """
    Determines whether to generate an answer or transform the query
    based on document relevance.
    """
    print("---ASSESS GRADED DOCUMENTS---")
    web_search = state["web_search"]
    
    if web_search == "Yes":
        print("---DECISION: TRANSFORM QUERY---")
        return "transform_query"
    else:
        print("---DECISION: GENERATE---")
        return "generate"

# Build the LangGraph workflow
def build_workflow(chatbot):
    """Build the chatbot workflow."""
    workflow = StateGraph(State)

    # Nodes
    workflow.add_node("retrieve", lambda s: retrieve(chatbot, s))
    workflow.add_node("grade_documents", lambda s: grade_documents(chatbot, s))
    workflow.add_node("generate", lambda s: generate(chatbot, s))
    workflow.add_node("transform_query", lambda s: transform_query(chatbot, s))
    workflow.add_node("web_search_node", lambda s: web_search(chatbot, s))

    # Edges
    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "grade_documents")

    # Conditional branching
    workflow.add_conditional_edges(
        "grade_documents",
        decide_to_generate,
        {
            "transform_query": "transform_query",
            "generate": "generate"
        }
    )

    workflow.add_edge("transform_query", "web_search_node")
    workflow.add_edge("web_search_node", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()
