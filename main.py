import streamlit as st
from chatbot.chatbot import ChatBot

# Initialize the chatbot and workflow
chatbot = ChatBot()
workflow = chatbot.build_workflow()

# Set up the app title and layout
st.set_page_config(
    page_title="AI ChatBot with LangGraph",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header and description
def display_header():
    st.title("🤖 AI ChatBot Powered by LangGraph")
    st.markdown(
        """
        Welcome to the AI ChatBot! This chatbot retrieves information, evaluates relevance, and generates meaningful responses to your queries.
        - **Ask about AI concepts, tools, or general topics.**
        - **Uses advanced retrieval and reasoning capabilities for accurate answers.**
        """
    )

# Sidebar options
def display_sidebar():
    st.sidebar.header("ChatBot Options")
    theme = st.sidebar.radio(
        "Choose a Theme:",
        ("Light", "Dark"),
        index=0,
        help="Select your preferred theme for the chatbot interface."
    )

    feedback_option = st.sidebar.checkbox("Enable Feedback", value=True)
    web_search_option = st.sidebar.checkbox(
        "Enable Web Search", value=True, help="Include web search results for better answers."
    )
    return feedback_option, web_search_option

# Chatbot input and processing
def handle_chatbot(web_search_option):
    st.markdown("### Enter Your Question Below:")
    question = st.text_input("Type your question here:", key="user_question", help="Ask any question related to AI, technology, or general topics.")

    if st.button("🤔 Get Answer"):
        if question:
            st.markdown("### 🛠️ Processing your question...")

            input_data = {"question": question}

            # Disable web search if the option is unchecked
            if not web_search_option:
                chatbot.web_search_tool.k = 0  

            # Run the chatbot workflow
            response = workflow.invoke(input_data)

            # Display the generated answer
            st.markdown("### 🤖 ChatBot's Answer:")
            st.success(response["generation"])
        else:
            st.warning("Please enter a question to get an answer.")

# Feedback section
def handle_feedback(feedback_option):
    if feedback_option:
        st.markdown("### 📢 Feedback")
        feedback = st.text_area("What do you think about the answer?", key="user_feedback")
        if st.button("Submit Feedback"):
            if feedback:
                st.success("Thank you for your feedback! 🙌")
            else:
                st.warning("Please provide feedback before submitting.")

# Footer
def display_footer():
    st.markdown("---")
    st.caption("Powered by Streamlit, LangGraph, and LangChain")

# Main function to run the Streamlit app
def main():
    display_header()
    feedback_option, web_search_option = display_sidebar()
    handle_chatbot(web_search_option)
    handle_feedback(feedback_option)
    display_footer()

if __name__ == "__main__":
    main()
