import asyncio
import aiohttp
import streamlit as st
import pandas as pd
from config import base_config
BACKEND_URL=base_config.BACKEND_URL_DEV

def smc_out():
    st.title("Отображение записей SMC")
    reports = asyncio.run(get_smc_ports())
    report_name = st.selectbox("Выберите отчет", reports)
    report = asyncio.run(get_smc_report(report_name))
    st.write(report)
   
    

async def get_smc_ports():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BACKEND_URL+'/api/smc/reports') as resp :
            resp.raise_for_status()
            response_data = await resp.json()
            return response_data

async def get_smc_report(report_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BACKEND_URL+f'/api/smc/report', params={"file_name": report_name}) as resp :
            resp.raise_for_status()
            response_data = await resp.json()
            return response_data