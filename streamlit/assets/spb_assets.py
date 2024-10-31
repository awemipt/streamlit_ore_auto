import streamlit as st

from logic_pages import smc_out


def spb_pages():
    page = st.sidebar.radio("Страницы", ["SMC_view", "test_page"])
    if page == "SMC_view":
        smc_out()
    elif page == "test_page":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: SPB")

