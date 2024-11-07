import extra_streamlit_components as stx
import streamlit as st


@st.cache_resource
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()