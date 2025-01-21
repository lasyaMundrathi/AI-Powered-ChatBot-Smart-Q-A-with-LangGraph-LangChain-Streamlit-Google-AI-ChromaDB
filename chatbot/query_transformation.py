from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def transform_query(chatbot, state):
    """Transform the question to a more optimal version."""
    print("---TRANSFORM QUERY---")
    system = """You are a question re-writer that converts an input question to a better version optimized for web search."""

    re_write_prompt = ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", "Here is the initial question: \n\n {question} \n Formulate an improved question.")
    ])

    question_rewriter = re_write_prompt | chatbot.llm | StrOutputParser()
    better_question = question_rewriter.invoke({"question": state["question"]})

    return {"documents": state["documents"], "question": better_question}
