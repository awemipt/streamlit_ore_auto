import streamlit as st

from utils import login_

def login_page():
    st.title("Авторизация")
    username = st.text_input("Имя пользователя")
    password = st.text_input("Пароль", type="password")
    login_button = st.button("Войти", on_click=login_, args=[username, password])
