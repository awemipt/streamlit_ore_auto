import streamlit as st

def chita_pages():
    page = st.sidebar.radio("Страницы", ["Page 1", "Page 2", "Page 3"])
    if page == "Page 1":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Chita")
    elif page == "Page 2":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Chita")
    elif page == "Page 3":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Chita")