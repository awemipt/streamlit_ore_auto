import streamlit as st
from manager_cookie import cookie_manager
from utils import login_

def login_page():
    st.title("Авторизация")
    username = st.text_input("Имя пользователя")
    password = st.text_input("Пароль", type="password")
    login_button = st.button("Войти")
    if login_button:
        login_(username, password)
