from langchain import hub
from langchain_core.output_parsers import StrOutputParser

def generate(chatbot, state):
    """Generate an answer based on the question and relevant documents."""
    print("---GENERATE---")
    prompt = hub.pull("rlm/rag-prompt")
    rag_chain = prompt | chatbot.llm | StrOutputParser()

    question = state["question"]
    documents = state["documents"]
    generation = rag_chain.invoke({"context": documents, "question": question})

    return {"documents": documents, "question": question, "generation": generation}
    
