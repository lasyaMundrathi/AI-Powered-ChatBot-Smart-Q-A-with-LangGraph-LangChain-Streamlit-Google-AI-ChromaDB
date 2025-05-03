### 🤖 AI ChatBot with LangGraph, LangChain, Streamlit, Google AI, and ChromaDB

## 🌟 Overview

This AI-powered chatbot leverages state-of-the-art technologies to provide intelligent information retrieval and response generation. Using LangGraph, LangChain, Streamlit, Google Generative AI, and ChromaDB, the chatbot efficiently retrieves relevant documents, grades their relevance, and generates meaningful responses.
## Architecture

<img src="https://github.com/user-attachments/assets/ae101545-c3e7-4721-8730-ceecab904b43" width="500"/>




## 🔄 Workflow Breakdown

### 🧾 User Input
A user submits a query via the **Streamlit** interface.

---

### 📥 Initial Retrieval
- The system searches internal documents using the **Chroma** vector store.
- Retrieved documents are **split into chunks** for efficient semantic processing.

---

### 🧠 Relevance Grading
- Each document chunk is evaluated for **relevance** using the **LLM**.
- **Irrelevant documents are discarded** to ensure high answer quality.

---

### ✍️ Query Transformation *(if necessary)*
- If no relevant documents are found, the original query is **rephrased** using the LLM.
- The goal is to **optimize it for search** (especially for external data).

---

### 🌐 Web Search *(if enabled)*
- The transformed query is used to perform a **web search via Tavily**.
- The retrieved results are **added to the document pool** for final reasoning.

---

### 🧩 Answer Generation
- The LLM (e.g., Google Gemini) generates a response based on the **final set of relevant documents**.

---

### 💬 Feedback Collection
- Users can optionally **submit feedback** on the response.
- This aids in **evaluating system performance** and planning future improvements.

## 🚀 Features

- 💡 Smart Q&A: Ask questions related to AI, technology, and general topics.

- 🔍 Intelligent Retrieval: Uses ChromaDB to retrieve relevant information.

- ✅ Document Grading: Filters relevant documents using AI-powered assessment.

- ✨ Query Optimization: Enhances search queries for better results.

- 🌐 Web Search Integration: Option to include web-based results.

- 📝 User Feedback: Collect feedback for continuous improvement.

- 🎨 Streamlit UI: Simple and interactive web-based interface.

  ## 🛠️ Technologies Used

- 🧠 LangGraph: For workflow management and state transitions.

- 🔗 LangChain: For advanced retrieval-augmented generation (RAG).

- 🌐 Streamlit: For an interactive and user-friendly chatbot interface.

- 🤖 Google Generative AI: For document embeddings and text generation.

- 📂 ChromaDB: Vector store for document retrieval and storage.

- 🔎 Tavily Search API: Enables web search for enhanced responses.


## Project Structure
```
│-- chatbot/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── retrieval.py
│   ├── grading.py
│   ├── generation.py
│   ├── query_transformation.py
│   ├── web_search.py
│   ├── workflow.py
│-- main.py
│-- requirements.txt
│-- README.md
```
## 📖 Usage

- 🖥️ Open the chatbot application in your browser.

- ❓ Enter a question related to AI, technology, or general topics.

- ⚙️ Choose options such as enabling web search and feedback.

- 🚀 Click "Get Answer" to receive an intelligent response.

- 📝 Provide feedback if desired.

```bash
# Clone the repository
git clone https://github.com/your-repo/chatbot-app.git
cd chatbot-app

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables (ensure .env file exists with API keys)
echo "GOOGLE_API_KEY=your_google_api_key" > .env
echo "TAVILY_API_KEY=your_tavily_api_key" >> .env

# Run the chatbot application
streamlit run main.py
```
