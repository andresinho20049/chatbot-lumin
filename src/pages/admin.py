import streamlit as st
from utils.database_func import storeData, getData
from utils.model_func import chatService, getContext

st.header("Lumin AI Assistant Admin Panel")

text_input = st.text_area("Enter text:", height=100)
store_button = st.button("Save")
get_data_button = st.button("Get Model")
get_context = st.button("Get Context")

if store_button:
    storeData(text_input)

if get_data_button:
    response = chatService(getData())
    st.write_stream(response)

if get_context:
    response = getContext()
    st.write_stream(response)