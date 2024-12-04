import streamlit as st
import pandas as pd
import io   
import traceback
import aiohttp
BACKEND_URL = st.secrets["BACKEND_URL_DEV"]
def load_excel():
    uploaded_file = st.file_uploader("Загрузите Excel файл с данными DWT", type=['xlsx', 'xls'])
    
    if uploaded_file:
        try:
            bytes_data = io.BytesIO(uploaded_file.getvalue())
            
            # Читаем Excel файл с помощью pandas
            excel_file = pd.ExcelFile(bytes_data)
            sheet_names = excel_file.sheet_names
            
            # Добавляем выпадающий список для выбора листа
            selected_sheet = st.selectbox("Выберите лист", sheet_names)
            
            st.success("Файл успешно загружен!")
            return excel_file
            
        except Exception as e:
            st.error(f"Ошибка при загрузке файла. \n {traceback.format_exc()}")
            return None
    
    return None

async def send_excel_to_backend(excel_file):
    try:
        excel_bytes = excel_file.read()
        files = {'file': ('data.xlsx', excel_bytes, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
        
        async with aiohttp.ClientSession() as session:
            async with session.post('http://{}/api/dwt/upload_excel', data=files) as response:
                if response.status == 200:
                    st.success("Файл успешно отправлен на сервер")
                    return await response.json()
                else:
                    st.error(f"Ошибка при отправке файла: {response.status}")
                    return None
                    
    except Exception as e:
        st.error(f"Ошибка при отправке файла: {str(e)}")
        return None

def dwt_input_excel():
    excel_file = load_excel()
    if excel_file is not None:
        st.write("Предпросмотр данных:")
        df = excel_file.parse(excel_file.sheet_names[0])  # Берем первый лист по умолчанию
        st.data_editor(df)
        st.write(df.head())