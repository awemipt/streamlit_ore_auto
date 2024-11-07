import hashlib
import json
import aiohttp
from manager_cookie import controller
from config import base_config

import streamlit as st
import asyncio

BACKEND_URL = base_config.BACKEND_URL_DEV 

def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    password_hash = hash_object.hexdigest()
    return password_hash

async def authenticate(username, password) -> str:
    pass_hash = hash_password(password=password)
    data = {
        "username": username,
        "pass_hash": pass_hash
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url=BACKEND_URL+"login", json=data) as resp :
            resp.raise_for_status()
            response_data = await resp.json()
            role = response_data.get('role')
    
    return role

def login_(username, password):
    try:
        role = asyncio.run(authenticate(username, password))
        
    except Exception as e:
        st.error(str(e))
        role = None
    if role:
        st.session_state["authenticated"] = True
        st.session_state["username"] = username
        st.session_state["role"] = role
        controller.set("authenticated", True)
        controller.set("role", role)
        
        st.success(f"Вы успешно вошли как {role}")
        
        st.rerun()
    else:
        st.error("Неверное имя пользователя или пароль")
def reset():
    st.session_state["authenticated"] = False
    controller.remove("authenticated")
    st.session_state["role"] = None
    controller.remove('role') 
    st.rerun()

def exit_():
    st.sidebar.button("Выйти", on_click=reset)
