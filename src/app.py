import streamlit as st
from utils.model_func import chatServiceStream
from utils.database_func import getValueByKey

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True) 

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = ["User", "Admin"]

def login():
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()

def home_page():
    pt_question = "Quais são as curiosidades sobre o dia de hoje, sou Brasileiro e gosto de ouvir curiosidades sobre o meu pais e em português. Resumo de até 100 caracteres"
    en_question = "What are the curiosities about today, I'm American and I like to hear curiosities about my country and in English. Summary of up to 100 characters"

    st.header("Wellcome :blue[Lumin]")
    with st.container():
        st.subheader('Curiosidade sobre o Brasil!')
        st.write_stream(chatServiceStream(pt_question))

    with st.container():
        st.subheader("Curiosity about America!")
        st.write_stream(chatServiceStream(en_question))


role = st.session_state.role

# Define pages
logout_page = st.Page(
    logout, 
    title="Log out", 
    icon=":material/logout:"
)
settings = st.Page(
    "pages/settings.py", 
    title="Settings", 
    icon=":material/settings:"
)
home = st.Page(
    home_page,
    title="Home",
    icon=":material/home:",
    default=(role == "User"),
)
chat = st.Page(
    "pages/chat.py",
    title="ChatBot",
    icon=":material/chat:"
)
admin = st.Page(
    "pages/admin.py",
    title="Admin",
    icon=":material/security:",
    default=(role == "Admin"),
)

account_pages = [logout_page, settings]
user_page = [home, chat]
admin_pages = [admin]

st.title("ChatLumin")
st.logo(
    "https://github.com/andresinho20049/andresinho20049/blob/present/public/Logo_extended.png?raw=true",
    link="https://andresinho20049.com.br/",
    icon_image="https://github.com/andresinho20049/andresinho20049/blob/present/public/Logo.png?raw=true",
)

st.session_state.model_name = getValueByKey("model_name") if getValueByKey("model_name")  is not None else "andresinho20049/lumin"
st.session_state.base_url = getValueByKey("base_url") if getValueByKey("base_url")  is not None else "http://ollama:11434"

page_dict = {}
if st.session_state.role in ["User", "Admin"]:
    page_dict["User"] = user_page
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict, position="sidebar", expanded=False)
    with st.sidebar:
        st.write(f"Model :blue[ {st.session_state.model_name} ] :robot_face:")
        st.write(f"Url :blue[{st.session_state.base_url}]")
else:
    pg = st.navigation([st.Page(login)])

pg.run()