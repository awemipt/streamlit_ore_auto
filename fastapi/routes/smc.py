import traceback
from fastapi import APIRouter, HTTPException
import aiofiles
import asyncio
import os
from utils import read_json_async
from crud import create_SMC, get_SMC
from core import get_db
# from LogstashJsonSocketHandler import get_logger
# logger = get_logger(__name__)
from config import base_config
router = APIRouter()


@router.post('/')
async def input(data: dict):
    try:
        await create_SMC(data=data, db= await get_db())    
    except Exception as e:
        print("error" , traceback.format_exc())
    else:
        return {"status": 'success'}

@router.get("/")
async def get_smc_records(limit: int = 10, offset: int = 0):
    result = await get_SMC(db=await get_db(), limit=limit, offset=offset)
    records =  result.scalars().all()
    return records