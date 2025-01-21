from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
import chromadb
from chromadb.config import Settings

def retrieve(chatbot, state):
    """Retrieve documents based on the question."""
    print("---RETRIEVE---")
    urls = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
        "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    ]
    
    # Improved WebBaseLoader with error handling
    docs = []
    for url in urls:
        try:
            loader = WebBaseLoader(url)
            loader.requests_kwargs = {'verify': False}  # Bypass SSL verification if needed
            docs.extend(loader.load())
        except Exception as e:
            print(f"Error loading {url}: {e}")
    
    # Split documents
    docs_splits = chatbot.text_splitter.split_documents(docs)

    # Chroma initialization with robust configuration
    try:
        # Create Chroma client with custom settings
        chroma_client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="./chroma_db"
        ))

        # Create Chroma vectorstore
        vectorstore = Chroma.from_documents(
            documents=docs_splits, 
            collection_name="rag-chroma", 
            embedding=chatbot.embeddings,
            client=chroma_client,
            persist_directory="./chroma_db"
        )
        
        # Create retriever
        retriever = vectorstore.as_retriever(
            search_type="mmr",  # Maximum Marginal Relevance retrieval
            search_kwargs={"k": 5}  # Retrieve top 5 most relevant documents
        )

        # Retrieve documents based on question
        question = state["question"]
        documents = retriever.invoke(question)

        return {"documents": documents, "question": question}
    
    except Exception as e:
        print(f"Error creating vectorstore: {e}")
        return {"documents": [], "question": state["question"]}
