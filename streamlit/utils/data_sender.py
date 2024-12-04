

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

async def send_excel_to_backend(excel_file, endpoint):
    excel_bytes = excel_file.read()
    
    files = {'file': (excel_file.name, excel_bytes, 'application/vnd.ms-excel')}
    
    # Отправляем POST запрос на бэкенд
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://{BACKEND_URL}/api/upload_excel', data=files) as response:
            if response.status == 200:
                st.success("Файл успешно отправлен на сервер")
                return await response.json()
            else:
                st.error(f"Ошибка при отправке файла: {response.status}")
                return None