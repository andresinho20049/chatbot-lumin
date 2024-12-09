import streamlit as st
from utils.database_func import setValueByKey

with st.form("settings_form", clear_on_submit=True):
    st.subheader('Setting Form!')
    
    model_name = st.text_input("Model Name", value="", key="input_model", placeholder="Enter the Model Name...", disabled=False, label_visibility="visible")
    model_url = st.text_input("Model Url", value="", key="input_url", placeholder="Enter the Model Url...", disabled=False, label_visibility="visible")

    submitted = st.form_submit_button("Save")
    if submitted:
        setValueByKey("model_name", model_name)
        setValueByKey("base_url", model_url)
        st.toast("New settings saved successfully!")
        st.rerun()

with st.container(border=True):
    st.markdown('''
                ## Chat Lumin Configuration

                **Important Notes:**
                * **Model Compatibility:** The Chat Lumin has been designed to work seamlessly with Ollama server-side models.
                * **No API Key Required:** Unlike other chatbots, the Chat Lumin does not require an API key for model operation.
                * **Docker Container Considerations:** For applications running in a Docker container, please use the service name (e.g. "http://ollama:11434") instead of "http://localhost:11434" to ensure proper connection establishment.
                * **Admin Access:** Administrators can upload new context data to the model, enabling enhanced functionality and customization.
                ''')