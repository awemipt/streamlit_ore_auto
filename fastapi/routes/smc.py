import traceback
from fastapi import APIRouter, HTTPException
import aiofiles
import asyncio
import os
from utils import read_json_async
from crud.cruds import create_SMC, get_SMC, create_SMC_report, create_SMC_raw_data
from core import get_db

from config import base_config
from fastapi import UploadFile, File, Form
router = APIRouter()
import pandas as pd
import io
from logic import smc_parser, get_A_b_params, calculate_params_from_ab

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
async def upload_excel( file: UploadFile, username: str = Form(...), file_name: str = Form(...)):
    try:
        bytes_data = io.BytesIO(file.file.read())
        excel_file = pd.ExcelFile(bytes_data, engine='openpyxl')
        print(file_name)
        res, SG = smc_parser(excel_file)
        A, b = get_A_b_params(res)
        
    except Exception as e:
        raise HTTPException(403, "invalid file")
    else:
        DWI, SCSE, t_a, M_ia, M_ic, M_ih = calculate_params_from_ab(A, b, SG)
        tasks = [asyncio.create_task(create_SMC_report(data={"A": A,
                                                              "b": b, 
                                                              "SG": SG, 
                                                              "DWI": DWI, 
                                                              "SCSE": SCSE, 
                                                              "t_a": t_a, 
                                                              "M_ia": M_ia, 
                                                              "M_ic": M_ic, 
                                                              "M_ih": M_ih,
                                                              "file_name": file_name.split('.')[0]+'_report'}, 
                                                              db=await get_db())),
                    asyncio.create_task(create_SMC_raw_data(data={'file': bytes_data.getvalue(), 
                                                                  'username': username, 
                                                                  'file_name': file_name}, 
                                                                  db=await get_db()))]
        await asyncio.gather(*tasks)
    
    return {"status": "success"}