import traceback
from fastapi import APIRouter, HTTPException
from crud import create_DWT_RESULT, get_SMC, get_DWT_samples
from core import get_db
from crud.data_from_table import get_t10_data
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

@router.get('/dwt-samples')
async def get_dwt_samples():    
    try:
        db = await get_db()
        return await get_DWT_samples(db=db)
    finally:
        await db.close()  #

@router.get('/dwt-data/get_sample')
async def get_dwt_sample(sample_name: str):
    try:
        db = await get_db()
        res = await get_t10_data(db=db, sample_name=sample_name)
        return res
    finally:
        await db.close()  #