from langchain.schema import Document

def web_search(chatbot, state):
    """Perform a web search based on the transformed query."""
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]

    docs = chatbot.web_search_tool.invoke({"query": question})
    web_results = "\n".join([d["content"] for d in docs])
    web_results = Document(page_content=web_results)
    documents.append(web_results)

    return {"documents": documents, "question": question}
