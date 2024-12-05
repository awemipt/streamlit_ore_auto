import streamlit as st
import pandas as pd
import io   
import traceback

from utils.data_sender import _send_excel

def load_excel():
    uploaded_file = st.file_uploader("Загрузите Excel файл с данными DWT теста", type=['xlsx', 'xls'])
    
    if uploaded_file:
        try:
            bytes_data = io.BytesIO(uploaded_file.getvalue())
            
            excel_file = pd.ExcelFile(bytes_data)
            sheet_names = excel_file.sheet_names
            
            
            st.success("Файл успешно загружен!")
            return excel_file
            
        except Exception as e:
            st.error(f"Ошибка при загрузке файла. \n {traceback.format_exc()}")
            return None
    
    return None


def dwt_input_excel():
    excel_file = load_excel()
    if excel_file is not None:
        st.write("Предпросмотр данных:")
        df = excel_file.parse(excel_file.sheet_names[0])  # Берем первый лист по умолчанию
        st.data_editor(df)
        st.write(df.head())
    if st.button("Отравить данные"):
        _send_excel(excel_file, "dwt/upload_excel")