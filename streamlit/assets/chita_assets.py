import streamlit as st
from logic_pages import smc_input, smc_out, dwt_input, smc_input_excel, dwt_input_excel, dwt_out
def chita_pages():
    page = st.sidebar.radio("Страницы", ["SMC", "DWT", "SMC_excel", "DWT_excel", "smc_out", "dwt_out"])
    if page == "SMC":
        smc_input()
    elif page == "DWT":
        dwt_input()
    elif page == "SMC_excel":
        smc_input_excel()
    elif page == "DWT_excel":
        dwt_input_excel()
    elif page == "smc_out":
        smc_out()
    elif page == "dwt_out":
        dwt_out()
    else:
        st.write("Страница не найдена")