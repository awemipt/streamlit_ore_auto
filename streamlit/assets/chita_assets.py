import streamlit as st
from logic_pages import smc_input, smc_out, dwt_input
def chita_pages():
    page = st.sidebar.radio("Страницы", ["SMC", "SMC_view", "Page 3", "DWT"])
    if page == "SMC":
        smc_input()
            
    elif page == "SMC_view":
        smc_out()
        
    elif page == "Page 3":
        st.write("Эта страница может быть просмотрена только пользователем с ролью: Chita")
    elif page == "DWT":
        dwt_input()
        