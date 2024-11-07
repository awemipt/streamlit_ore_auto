import streamlit as st
import pandas as pd
data = None
import random

size_values = ["63 x 53", "45 x 37.5", "31.5 x 26.5", "22.4 x 19", "16 x 13.2"]
size_mm_map = {
        "63 x 53": [53.0, 37.5, 26.5, 19.0, 13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425, "Pallet"],
        "45 x 37.5": [37.5, 26.5, 19.0, 13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425, "Pallet"],
        "31.5 x 26.5": [26.5, 19.0, 13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425, "Pallet"],
        "22.4 x 19": [19.0, 13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425, "Pallet"],
        "16 x 13.2": [13.2, 9.50, 6.70, 4.75, 3.35, 2.36, 1.70, 1.18, 0.850, 0.600, 0.425, "Pallet"]
    }
if "data_cache" not in st.session_state:
    st.session_state["data_cache"] = {}


def dwt_form_energy_or_size_change():
    selected_size = st.session_state["selected_size"]
    input_energy = st.session_state["dwt_energy"]

    cache_key = (selected_size, input_energy)
    if cache_key in st.session_state["data_cache"]:
        st.session_state["data"] = st.session_state["data_cache"][cache_key]
    else:
        size_mm = size_mm_map[selected_size]
        initial_data = pd.DataFrame({
            "Size (mm)": size_mm,
            "Retention Weight (g)": [0.0] * len(size_mm),
            "Energy Percentage (%)": [0.0] * len(size_mm)
        })
        st.session_state["data"] = initial_data

def fill_with_random_values():
    if "data" in st.session_state:
        st.session_state["data"]["Retention Weight (g)"] = [
            random.uniform(0.0, 100.0) for _ in range(len(st.session_state["data"]))
        ]
        # Recalculate Energy Percentage based on new random values
        initial_weight = st.session_state.get("initial_weight", 0)
        if initial_weight > 0:
            st.session_state["data"]["Energy Percentage (%)"] = (
                st.session_state["data"]["Retention Weight (g)"] / initial_weight * 100
            )

def dwt_input():
   

    st.title("DWT Form")

    selected_size = st.selectbox("Select size :", size_values, on_change=dwt_form_energy_or_size_change, key='selected_size')
    
    input_energy = st.number_input("DWT_energy",  on_change=dwt_form_energy_or_size_change, key='dwt_energy')
    

    initial_weight = st.number_input("Enter Initial Sample Weight (g):", min_value=0.0, format="%.2f")

    if "data" in st.session_state:
        edited_data = st.session_state["data"]
    else:
        size_mm = size_mm_map[selected_size]
        edited_data = pd.DataFrame({
            "Size (mm)": size_mm,
            "Retention Weight (g)": [0.0] * len(size_mm),
            "Energy Percentage (%)": [0.0] * len(size_mm)
        })
        st.session_state["data"] = edited_data

    st.write("Input Retention Weights in the table below:")
    edited_data = st.data_editor(edited_data, num_rows="dynamic")

   
    if initial_weight > 0:
        edited_data["Energy Percentage (%)"] = (edited_data["Retention Weight (g)"] / initial_weight) * 100


    cache_key = (selected_size, input_energy)
    st.session_state["data_cache"][cache_key] = edited_data

    

    st.button("Fill with Random Values", on_click=fill_with_random_values)
