

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