import io

from os import environ
from PIL import Image

import streamlit as st

# Словарь с логинами, паролями и ролями пользователей
users = {
    "admin": {"password": "admin_pass", "role": "admin"},
    "chita_user": {"password": "chita_pass", "role": "Chita"},
    "spb_user": {"password": "spb_pass", "role": "Spb"}
}

def authenticate(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

def login():
    st.title("Авторизация")

    username = st.text_input("Имя пользователя")
    password = st.text_input("Пароль", type="password")
    login_button = st.button("Войти")

    if login_button:
        role = authenticate(username, password)
        if role:
            st.session_state["authenticated"] = True
            st.session_state["role"] = role
            st.success(f"Вы успешно вошли как {role}")
            st.experimental_rerun()
        else:
            st.error("Неверное имя пользователя или пароль")

def check_access(required_role):
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.warning("Пожалуйста, войдите в систему.")
        st.stop()

    role = st.session_state.get("role")
    if role != required_role and role != "admin":
        st.warning("У вас нет доступа к этой странице.")
        st.stop()

def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        login()
    else:
        role = st.session_state["role"]

        if role == "admin":
            st.title("Админская панель")
            st.write("У вас полный доступ ко всем функциям приложения.")
            

        elif role == "Chita":
            st.title("Панель пользователя Chita")
            st.write("У вас доступ к функциям, разрешенным для Chita.")
            

        elif role == "Spb":
            st.title("Панель пользователя Spb")
            st.write("У вас доступ к функциям, разрешенным для Spb.")
            

        
        if st.button("Выйти"):
            st.session_state["authenticated"] = False
            st.session_state["role"] = None
            st.experimental_rerun()
main()