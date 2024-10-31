import streamlit as st

def spb_pages():
    page = st.sidebar.radio("Страницы", ["Page 1", "Page 2"])
    
    if page == "Page 1":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: SPB")
    elif page == "Page 2":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: SPB")

