import streamlit as st
from manager_cookie import cookie_manager
from utils import login_

def login_page():
    st.title("Авторизация")
    st.text(cookie_manager.get_all())
    username = st.text_input("Имя пользователя")
    password = st.text_input("Пароль", type="password")
    login_button = st.button("Войти", on_click=login_, args=[username, password])
