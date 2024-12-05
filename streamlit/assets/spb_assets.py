import streamlit as st

from logic_pages import smc_out, dwt_view_page


def spb_pages():
    page = st.sidebar.radio("Страницы", ["SMC_view", "test_page", "dwt_view"])
    if page == "SMC_view":
        smc_out()
    elif page == "test_page":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: SPB")
    elif page == "dwt_view":
        dwt_view_page()
    elif page == "smc_view":
        smc_out()