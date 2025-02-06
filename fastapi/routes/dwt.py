import traceback
from fastapi import APIRouter, HTTPException
from crud import create_DWT_RESULT, get_SMC, get_DWT_samples, create_DWT_report, create_DWT_raw_data
from core import get_db
from sqlalchemy import select
from models import DWT_RESULT,DWT_REPORT
from crud.data_from_table import get_t10_data
from config import base_config
import pandas as pd
from logic import get_ore_params
import io
from logic import dwt_parser, get_A_b_params, calculate_params_from_ab
from fastapi import UploadFile, Form
import asyncio
from crud import  get_DWT_report, get_DWT_reports_list
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
        return [
        {
            "id": report.id,
            "name": report.name,
            "created_at": report.created_at.strftime("%Y-%m-%d %H:%M"),
            # другие поля
        }
        for report in await db.execute(query=DWT_RESULT.select())
        ]
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

@router.post("/upload_excel")
async def upload_excel( file: UploadFile, username: str = Form(...), file_name: str = Form(...)):
    try:
        bytes_data = io.BytesIO(file.file.read())
        excel_file = pd.ExcelFile(bytes_data)
        retentions, energies, sizes, SG = dwt_parser(excel_file)

        ore_params = get_ore_params(retentions, energies, sizes, SG)
        print(ore_params)
        A, b = get_A_b_params(ore_params)
        print(A, b)
        
    except Exception as e:
        raise HTTPException(403, "invalid file")
    else:
        DWI, SCSE, t_a, M_ia, M_ic, M_ih = calculate_params_from_ab(A, b, SG)
        tasks = [asyncio.create_task(create_DWT_report(data={"A": A,
                                                              "b": b, 
                                                              "SG": SG, 
                                                              "DWI": DWI, 
                                                              "SCSE": SCSE, 
                                                              "t_a": t_a, 
                                                              "M_ia": M_ia, 
                                                              "M_ic": M_ic, 
                                                              "M_ih": M_ih,
                                                              "file_name": file_name.split('.')[0]+'_report',
                                                              "T_10": ore_params.t10,
                                                              "Energies": ore_params.energy,
                                                              "Sizes": sizes}, 
                                                              db=await get_db())),
                    asyncio.create_task(create_DWT_raw_data(data={'file': bytes_data.getvalue(), 
                                                                  'username': username, 
                                                                  'file_name': file_name}, 
                                                                  db=await get_db()))]
        await asyncio.gather(*tasks)
    
    return ore_params

@router.get("/reports")
async def get_reports_list():
    # return await get_DWT_reports_list(db=await get_db())
    db = await get_db()
    try:
        async with db:
            query =  select(DWT_REPORT.id, DWT_REPORT.file_name)
            result = await db.execute(query)
            curr = result.fetchall()
            
            return [
            {
                "id": report[0],
                "name": report[1],
                
                
            }
            for report in curr]
    except:
        pass

@router.get("/report")
async def get_report(report_id: int):
    db = await get_db()
    query = select(DWT_REPORT).where(DWT_REPORT.id == report_id)

    result = await db.execute(query)
    curr = [dict(row._mapping) for row in result]
    graph_data = []
    return curr
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return dict(report)