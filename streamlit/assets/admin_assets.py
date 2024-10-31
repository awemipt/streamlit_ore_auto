import streamlit as st

from logic_pages import smc_input, smc_out

def admin_pages():
    page = st.sidebar.radio("Страницы", ["SMC", "SMC_view", "User Management"])
    if page == "SMC":
        smc_input()
            
    elif page == "SMC_view":
        smc_out()
    elif page == "User Management":
        st.write("Страница управления пользователями, доступная только для роли: Admin")