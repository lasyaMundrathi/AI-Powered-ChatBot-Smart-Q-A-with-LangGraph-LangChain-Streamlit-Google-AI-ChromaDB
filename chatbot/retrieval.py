from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
import chromadb

def retrieve(chatbot, state):
    """Retrieve documents based on the question."""
    print("---RETRIEVE---")
    urls = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
        "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    ]
    
    # Load documents
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]
    docs_splits = chatbot.text_splitter.split_documents(docs_list)

    # Create Chroma vectorstore
    vectorstore = Chroma.from_documents(
        documents=docs_splits, 
        collection_name="rag-chroma", 
        embedding=chatbot.embeddings, 
        persist_directory="./chroma_db"
    )
    
    # Create retriever
    retriever = vectorstore.as_retriever()

    question = state["question"]
    documents = retriever.invoke(question)

    return {"documents": documents, "question": question}
