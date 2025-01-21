from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class GradeDocuments(BaseModel):
    binary_score: str = Field(description="Documents are relevant to the question, 'yes' or 'no'")

def grade_documents(chatbot, state):
    """Grade documents based on relevance to the question."""
    print("---GRADE DOCUMENTS---")
    question = state["question"]
    documents = state["documents"]

    structured_llm_grader = chatbot.llm.with_structured_output(GradeDocuments)

    system = """You are a grader assessing relevance of a retrieved document to a user question. 
    If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant."""

    grade_prompt = ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question}")
    ])

    retrieval_grader = grade_prompt | structured_llm_grader

    filtered_docs = []
    web_search = "No"
    for d in documents:
        score = retrieval_grader.invoke({"question": question, "document": d.page_content})
        if score.binary_score == "yes":
            filtered_docs.append(d)
        else:
            web_search = "Yes"

    return {"documents": filtered_docs, "question": question, "web_search": web_search}
