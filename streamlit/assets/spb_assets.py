import streamlit as st

from logic_pages import smc_out, dwt_view_page


def spb_pages():
    page = st.sidebar.radio("Страницы", ["SMC_view", "dwt_view"])
    if page == "SMC_view":
        smc_out()
 
    elif page == "dwt_view":
        dwt_view_page()
  