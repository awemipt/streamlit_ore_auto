import numpy as np
import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
from os import getenv
from scipy.optimize import curve_fit
BACKEND_URL = getenv("BACKEND_URL_DEV")
def fit_function(energy, A, b):
    return A * (1 - np.exp(-b * energy))

def dwt_view_page():
    st.title("DWT Test Results")
    

    try:
        response = requests.get(f"{BACKEND_URL}/api/dwt/dwt-samples")
        if response.status_code == 200:
            samples = response.json()
        else:
            st.error("Не удалось получить список образцов")
            return
    except Exception as e:
        st.error(f"Ошибка при подключении к серверу: {str(e)}")
        return


    selected_sample = st.selectbox(
        "Выберите образец:",
        options=samples,
        key="dwt_sample_selector"
    )

    if selected_sample:
        try:
          
            response = requests.get(f"{BACKEND_URL}/api/dwt/dwt-data/get_sample", params={"sample_name": selected_sample})
            if response.status_code == 200:
                data = response.json()
                st.write('Сырые данные')
                st.write(data, )
                energies = [point["energy"] for point in data]
                retentions = [point["retention_at_t10"] for point in data]
            
                energies_array = np.array(energies)
                retentions_array = np.array(retentions)
                
                try:
                    popt, _ = curve_fit(fit_function, energies_array, retentions_array, p0=[100, 0.1])
                    A_opt, b_opt = popt
                    
                    energy_fit = np.linspace(min(energies), max(energies), 100)
                
                    retention_fit = fit_function(energy_fit, A_opt, b_opt)
                except Exception as e:
                    st.error(f"Ошибка при подборе параметров: {str(e)}")
                    return
                
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=energies,
                    y=retentions,
                    mode='markers',
                    name='t10 vs Energy'
                ))
                fig.add_trace(go.Scatter(
                    x=energy_fit,
                    y=retention_fit,
                    mode='lines',
                    name='Fit'
                ))
                fig.update_layout(
                    title="Зависимость t10 от энергии",
                    xaxis_title="Энергия (кВт⋅ч/т)",
                    yaxis_title="t10 (%)",
                    showlegend=True
                )

                st.plotly_chart(fig, use_container_width=True)
                st.write(f"Оптимальные параметры:")
                st.write(f"A = {A_opt:.2f}")
                st.write(f"b = {b_opt:.4f}")
            else:
                st.error(f"Не удалось получить данные для выбранного образца{response.status_code}")
        
        except Exception as e:
            st.error(f"Ошибка при получении данных: {str(e)}")