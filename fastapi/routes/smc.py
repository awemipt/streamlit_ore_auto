import traceback
from fastapi import APIRouter, HTTPException
import aiofiles
import asyncio
import os
from utils import read_json_async
from crud.cruds import create_SMC, get_SMC
from core import get_db
# from LogstashJsonSocketHandler import get_logger
# logger = get_logger(__name__)
from config import base_config
from fastapi import UploadFile, File, Form
router = APIRouter()
import pandas as pd
import io
from logic import smc_parser
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

@router.post("/upload_excel")
async def upload_excel( file: UploadFile, username: str = Form(...)):
    print(file.file)
    bytes_data = io.BytesIO(file.file.read())
    excel_file = pd.ExcelFile(bytes_data, engine='openpyxl')
    print(excel_file.sheet_names)
    res = smc_parser(excel_file)
    return {"status": "success"}