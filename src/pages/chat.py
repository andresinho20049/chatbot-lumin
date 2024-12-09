import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from utils.model_func import chatService, getModel
from utils.database_func import getData

st.header("_Streamlit_ is :blue[ChatBot Lumin] :robot_face:")

def getResponse(user_query, chat_history):

    previous_context = chatService(getData())

    template = """
    You are a helpful assistant. Please answer the following questions considering the conversation history and previous contexts.:

    Previous Context: {previous_context}
    
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