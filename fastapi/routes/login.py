from fastapi import APIRouter, HTTPException
import aiofiles
import asyncio
import os
from utils import read_json_async
# from LogstashJsonSocketHandler import get_logger
# logger = get_logger(__name__)
from config import base_config
router = APIRouter()


@router.post('/')
async def login(data: dict):
    
    pass_database = dict(await read_json_async(base_config.SECRETS_FILE_PATH))
    username = data.get("username")
    pass_hash = data.get("pass_hash")

   
    if not username:
        raise HTTPException(status_code=401, detail="Empty username")
    elif username not in pass_database:
        raise HTTPException(status_code=401, detail="User not found")
    elif pass_database[username].get('hashed_password') != pass_hash:
        raise HTTPException(status_code=401, detail="Invalid password",)
    else:
        print('success')
        return {"role": pass_database[username]['role']}
