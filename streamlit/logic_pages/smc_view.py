import asyncio
import aiohttp
import streamlit as st
import pandas as pd
from config import base_config
BACKEND_URL=base_config.BACKEND_URL_DEV

def smc_out():
    st.title("Отображение записей SMC")
    page_number = 0
    records_per_page = st.selectbox("Отображать записей на страницу:", [5, 10, 20, 50], index=1)
    if st.button("Следующая страница"):
        page_number += 1
    if st.button("Предыдущая страница") and page_number > 0:
        page_number -= 1
    offset = page_number * records_per_page
    data = asyncio.run(_get('/smc', records_per_page, offset))
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("Нет данных для отображения.")

async def _get(endpoint, limit, offset):
    params = {"limit": limit, "offset": offset}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BACKEND_URL+endpoint, params=params) as resp :
            resp.raise_for_status()
            response_data = await resp.json()
            return response_data