from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.tools.tavily_search import TavilySearchResults
import os

os.environ["USER_AGENT"] = "myagent"

class ChatBot:
    def __init__(self):
        """Initialize ChatBot with document retrieval and processing capabilities."""
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        self.web_search_tool = TavilySearchResults(k=3)
        self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=250, chunk_overlap=0
        )
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
