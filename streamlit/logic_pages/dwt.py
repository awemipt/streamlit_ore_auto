import streamlit as st
import pandas as pd

data = None
import random
import asyncio
from utils.data_sender import _send
from manager_cookie import cookie_manager
size_values = ["63 x 53", "45 x 37.5", "31.5 x 26.5", "22.4 x 19", "16 x 13.2"]
size_mm_map = {
        "63 x 53": [53.0, 37.5, 26.5, 19.0, 13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425, "Pallet"],
        "45 x 37.5": [37.5,26.5,19.0,13.2,9.5,6.70,4.75,3.35,2.36,1.70,1.18,0.85,0.600,0.425,0.300, "Pallet"],
        "31.5 x 26.5": [26.5, 19.0, 13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425,0.300, 0.212, "Pallet"],
        "22.4 x 19": [19.0, 13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425,0.300, 0.212, 0.150 ,"Pallet"],
        "16 x 13.2": [13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425,0.300, 0.212, 0.150,0.106, "Pallet"]
    }
if "data_cache" not in st.session_state:
    st.session_state["data_cache"] = {}

def data_cache_to_cookie():
    cookie_manager.cookies['data_cache'] = st.session_state['data_cache']

def dwt_form_energy_or_size_change():
    # data_cache_to_cookie()
    sample_name = st.session_state['sample_name']
    selected_size = st.session_state["selected_size"]
    input_energy = st.session_state["dwt_energy"]

    cache_key = (sample_name, selected_size, input_energy)
    if cache_key in st.session_state["data_cache"]:
        st.session_state["data"] = st.session_state["data_cache"][cache_key]
    else:
        size_mm = size_mm_map[selected_size]
        initial_data = pd.DataFrame({
            "Size (mm)": size_mm,
            "Retention Weight (g)": [0.0] * len(size_mm),
            "Retention percentage (%)": [0.0] * len(size_mm),
            "Retention comulitive percentage (%)": [0.0] * len(size_mm)
        })
        st.session_state["data"] = initial_data


def fill_with_random_values():
    if "data" in st.session_state:
        st.session_state["data"]["Retention Weight (g)"] = [
            random.uniform(0.0, 100.0) for _ in range(len(st.session_state["data"]))
        ]


        initial_weight = st.session_state.get("initial_weight", 0)
        if initial_weight > 0:
            st.session_state["data"]["Energy Percentage (%)"] = (
                st.session_state["data"]["Retention Weight (g)"] / initial_weight * 100
            )
def submit(**kwargs):
    kwargs['data'] = kwargs["data"].to_dict()
    asyncio.run(_send(kwargs, endpoint="/dwt"))


def dwt_input():
    if "data_cache" not in st.session_state :
        if "data_cache" not in cookie_manager.cookies:
            st.session_state['data_cache'] = {}
        else:
            st.session_state["data_cache"] = cookie_manager.cookies['data_cache']

    st.title("DWT Form")
    sample_name = st.text_input("Name of sample",on_change=dwt_form_energy_or_size_change, key='sample_name')
    selected_size = st.selectbox("Select size :", size_values, on_change=dwt_form_energy_or_size_change, key='selected_size')
    
    input_energy = st.number_input("DWT_energy (kWh/h)",  on_change=dwt_form_energy_or_size_change, key='dwt_energy')
    

    initial_weight = st.number_input("Enter Initial Sample Weight (g):", min_value=0.0, format="%.2f")

    if "data" in st.session_state:
        edited_data = st.session_state["data"]
    else:
        size_mm = size_mm_map[selected_size]
        edited_data = pd.DataFrame({
            "Size (mm)": size_mm,
            "Retention Weight (g)": [0.0] * len(size_mm),
            "Retention percentage (%)": [0.0] * len(size_mm),
            "Retention comulitive percentage (%)": [0.0] * len(size_mm)
        })
        st.session_state["data"] = edited_data

    st.write("Input Retention Weights in the table below:")
    edited_data = st.data_editor(edited_data, column_config={"Size (mm)": "Size (mm)",
            "Retention Weight (g)": "Retention Weight (g)",
            "Retention percentage (%)": None,
            "Retention comulitive percentage (%)": None
            },height=600
            ,on_change=data_cache_to_cookie)

   
    st.subheader("result")
    total_weight = edited_data['Retention Weight (g)'].sum()
    if total_weight > 0:
        edited_data['Retention percentage (%)'] = (edited_data['Retention Weight (g)'] / total_weight) * 100
        edited_data['Retention comulitive percentage (%)'] = edited_data['Retention percentage (%)'].cumsum()
    else:
        edited_data['Retention percentage (%)'] = 0.0  
    st.write(edited_data,)

    cache_key = (sample_name, selected_size, input_energy)
    st.session_state["data_cache"][cache_key] = edited_data
    
    

    st.button("Fill with Random Values", on_click=fill_with_random_values)

    submitted = st.button("Submit data")
    if submitted:
        try:
            submit(data=edited_data,initial_weight=initial_weight, input_energy=input_energy, sample_name=sample_name)
        except Exception as e:
            st.error(f"Сервер не отвечает {e}")
        else: 
            st.success("Данные отправлены")