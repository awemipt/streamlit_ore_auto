

from datetime import datetime
import streamlit as st

import aiohttp

from message_models.models import Metadata
from utils.login import BACKEND_URL


async def _send(data: dict, endpoint: str):
    metadata = Metadata(
        username=st.session_state['username'], 
        created_timestamp=datetime.now().timestamp(), 
        ).model_dump()
    
    data.update(metadata)
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url=BACKEND_URL+endpoint, json=data) as resp :
            resp.raise_for_status()
            response_data = await resp.json()

async def _send_excel(data, file_name, endpoint):
    
    data = {'username': st.session_state['username'], 'file': data.getvalue(), 'file_name': file_name}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url=BACKEND_URL+endpoint, data=data) as response:
            if response.status == 200:
                st.success("Файл успешно отправлен на сервер")
                return await response.json()
            else:
                st.error(f"Ошибка при отправке файла: {response.status}")
                return None