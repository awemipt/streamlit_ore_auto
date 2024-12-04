import streamlit as st
import pandas as pd

import io   
import traceback
from openpyxl import load_workbook
def load_excel() -> pd.ExcelFile:
    uploaded_file = st.file_uploader("Загрузите защищенный Excel файл", type=['xlsm'])
    
    if uploaded_file:
        try:
            bytes_data = io.BytesIO(uploaded_file.getvalue())
            
            excel_file = pd.ExcelFile(bytes_data, engine='openpyxl')
            excel_file.name = uploaded_file.name
            
            
            
            
            st.success("Файл успешно загружен!")
            return excel_file
            
            
        except Exception as e:
            st.error(f"Ошибка при загрузке файла. \n {traceback.format_exc()}")
            return None
    
    return None
def smc_verify_excel(excel_file):
    return True

# Использование функции     
def smc_input_excel():
    excel_file = load_excel()
    sheets = excel_file.sheet_names
    if smc_verify_excel(excel_file):
        st.write("Предпросмотр данных:")
        selected_sheet = st.selectbox("Выберите лист", sheets)
        df = excel_file.parse(selected_sheet)
        st.data_editor(df)
        st.write(df.head)
