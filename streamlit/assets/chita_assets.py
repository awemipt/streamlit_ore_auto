import streamlit as st
from logic_pages import smc_input
def chita_pages():
    page = st.sidebar.radio("Страницы", ["SMC", "Page 2", "Page 3"])
    if page == "SMC":
       smc_input()
            
    elif page == "Page 2":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Chita")
    elif page == "Page 3":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Chita")