import asyncio
import traceback
import streamlit as st
import aiohttp
from datetime import datetime
from config import base_config
from pydantic import ValidationError
from message_models import SendSmcModel, Metadata
from utils.data_sender import _send
BACKEND_URL = base_config.BACKEND_URL_DEV 

def smc_input():
    with st.form("data_form"):
        name = st.text_input("Name")
        a = st.number_input("A", format="%.2f")
        b = st.number_input("B", format="%.2f")
        dwt = st.number_input("DWT", format="%.2f")
        smc = st.checkbox("SMC")
        comment = st.text_area("Comment")
        wirm_bond = st.number_input("WiRM Bond", format="%.2f")
        wirm_non_std = st.number_input("WiRM Non-Std", format="%.2f")

        submitted = st.form_submit_button("Submit")

        if submitted:
            data = {
                "name": name,
                "a": a,
                "b": b,
                "dwt": dwt,
                "smc": smc,
                "comment": comment,
                "wirm_bond": wirm_bond,
                "wirm_non_std": wirm_non_std
            }
            try:
                asyncio.run(_send(data, endpoint="/smc"))
            except ValidationError as e:
                st.error(f"Некорректные данные{traceback.format_exc()}")
            except Exception as e:
                st.error(f"сервер не отвечает {traceback.format_exc()}")
            else:
                st.success("Данные отправлены")

