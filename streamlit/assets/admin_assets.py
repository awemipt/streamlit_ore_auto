import streamlit as st

def admin_pages():
    page = st.sidebar.radio("Страницы", ["Page 1", "Page 2", "User Management"])
    if page == "Page 1":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Admin")
    elif page == "Page 2":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Admin")
    elif page == "User Management":
        st.write("Страница управления пользователями, доступная только для роли: Admin")