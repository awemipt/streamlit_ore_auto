import traceback
from fastapi import APIRouter, HTTPException
from crud import create_DWT_RESULT, get_SMC
from core import get_db

from config import base_config
router = APIRouter()


@router.post('/')
async def input(data: dict):
    try:
        await create_DWT_RESULT(data=data, db= await get_db())    
        #TODO ADD 
    except Exception as e:
        print("error" , traceback.format_exc())
    else:
        return {"status": 'success'}
