import streamlit as st

st.set_page_config(layout="wide")
import io
from os import environ
from PIL import Image
import asyncio

from assets import chita_pages, spb_pages, admin_pages, login_page
from utils import login_, exit_
from manager_cookie import cookie_manager


def check_access(required_role):
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.warning("Пожалуйста, войдите в систему.")
        st.stop()

    role = st.session_state.get("role")
    if role != required_role and role != "admin":
        st.warning("У вас нет доступа к этой странице.")
        st.stop()

def show_page_for_role(role):
    if role == "chita":
        st.sidebar.title("Меню Chita")
        
        chita_pages()
        exit_()

    elif role == "spb":
        st.sidebar.title("Меню SPB")
        spb_pages()
        exit_()
    elif role == "admin":
        st.sidebar.title("Меню Admin")
        admin_pages()
        exit_()
    else:
        st.write(role)
        st.write("Недоступная роль пользователя")

def make_sessionstate_from_cookies():
    cookies = cookie_manager.cookies
    # print(cookies)
    for key, value in cookies.items():
        st.session_state[key] = value
    pass

def main():
    
    make_sessionstate_from_cookies()
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        login_page()
    else:
        role =  st.session_state["role"] 
        show_page_for_role(role)        
    
   
if __name__ =="__main__":
    main()