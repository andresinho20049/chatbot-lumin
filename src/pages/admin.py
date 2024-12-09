import streamlit as st
from utils.database_func import storeData, getData
from utils.model_func import chatService, chatServiceStream, getContext

st.header("Lumin AI Assistant Admin Panel")

with st.form("admin_form", clear_on_submit=True):
    text_input = st.text_area("Enter text:", height=100)
    store_button = st.form_submit_button("Save")

cols = st.columns([2,1,2]) 
get_data_button = cols[0].button("Get Model")
with cols[2].popover("See Bot Context"):
    st.markdown(getContext())

if store_button:
    storeData(text_input)
    st.toast("Bot preferences saved successfully!")

if get_data_button:
    data = getData()
    st.write_stream(chatServiceStream(data))
    
    response = chatService(data)
    if response:
        with st.expander("See more"):
            st.write(response)
        st.session_state.context = response.content