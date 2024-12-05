import streamlit as st
import pandas as pd

import io   
import traceback
from openpyxl import load_workbook
from utils.data_sender import _send_excel
import asyncio
def load_excel() -> pd.ExcelFile:
    uploaded_file = st.file_uploader("Загрузите Excel файл с данными SMC теста", type=['xlsm'])
    
    if uploaded_file:
        try:
            bytes_data = io.BytesIO(uploaded_file.getvalue())
            
            excel_file = pd.ExcelFile(bytes_data, engine='openpyxl')
            bytes_data.name = uploaded_file.name
            excel_file.name = uploaded_file.name
            st.success("Файл успешно загружен!")
            return excel_file, bytes_data
            
            
        except Exception as e:
            st.error(f"Ошибка при загрузке файла. \n {traceback.format_exc()}")
            return None, None
    
    return None, None
def smc_verify_excel(excel_file):\
    #TODO VERIFICATION
    if excel_file is None:
        return False
    return True
 
def smc_input_excel():
    excel_file, bytes_data = load_excel()
    
    if smc_verify_excel(excel_file):
        sheets = excel_file.sheet_names
        res_sheet = sheets.index("Исходные данные")
        if res_sheet == -1:
            raise ValueError("Sheet 'Исходные данные' not found")
        df = pd.read_excel(excel_file, sheet_name=sheets[res_sheet])
        st.data_editor(df)
        st.write(df.index[1])
        st.write({key: value for key, value in zip(df[df.columns[1]][9:14], df[df.columns[2]][9:14])})
    if st.button("Отравить данные"):
        try:
            asyncio.run(_send_excel(bytes_data, "/api/smc/upload_excel"))
        except Exception as e:
            st.error(f"Ошибка при отправке данных. \n {traceback.format_exc()}")
        else:
            st.success("Данные успешно отправлены!")

