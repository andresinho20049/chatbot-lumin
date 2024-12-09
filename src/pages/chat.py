import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from utils.model_func import chatService, getModel
from utils.database_func import getData

# Initialize chat history
if "context" not in st.session_state:
    st.session_state.context = None

st.header("_Streamlit_ is :blue[ChatBot Lumin] :robot_face:")
previous_context = st.session_state.context if st.session_state.context is not None else ""

def getResponse(user_query, chat_history):

    template = """
    You are a helpful assistant. Please answer the following questions considering the conversation history and contexts.:

    You are given a user query, some textual context, chat history and rules, all inside xml tags. You have to answer the query based on the context while respecting the rules.

    Context: {previous_context}

    <rules>
    - If you don't know, just say so.
    - If you are not sure, ask for clarification.
    - Answer in the same language as the user query, and bring a translated version of the English answer if asked in another language.
    - If the context appears unreadable or of poor quality, tell the user then answer as best as you can.
    - If the answer is not in the context but you think you know the answer, explain that to the user then answer with your own knowledge.
    - Answer directly and without using xml tags.
    </rules>
        
    Chat history: {chat_history}

    User question: {user_question}

    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = getModel()
        
    chain = prompt | llm | StrOutputParser()

    return chain.stream({
        "previous_context": previous_context,
        "chat_history": chat_history,
        "user_question": user_query,
    })

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a Lumin Bot. How can I help you?"),
    ]

    
# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = st.write_stream(getResponse(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=response))