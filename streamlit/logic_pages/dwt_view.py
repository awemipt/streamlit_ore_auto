import numpy as np
import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
from os import getenv
from scipy.optimize import curve_fit
import asyncio, aiohttp
BACKEND_URL = getenv("BACKEND_URL_DEV")
import matplotlib.pyplot as plt

def fit_function(x, A, b):
    return (A * (1 - np.exp(-b * x)))

def dwt_out():
    st.title("Отображение записей DWT")
    reports = asyncio.run(get_dwt_reports())
    if reports:
        selected = st.selectbox(
            "Выберите отчет",
            options=reports,
            format_func=lambda x: f"{x['name']} ({x['id']})"  
        )
        
        if st.button("Показать отчет"):
            report = asyncio.run(get_dwt_report(selected['id']))[0]["DWT_REPORT"]
            st.write(report)
            A, b =  report["A"], report['b']
            t10 = np.array(report['T_10'])
            energies = np.array(report['Energies'])
            sizes = np.array(report['Sizes'])
            distinct_sizes = [size[0] for size in sizes]
            # # График 1: T10 vs Size[0] для разных энергий
            # st.header("Зависимость T10 от Size[0] для разных энергий")
            # fig1, ax1 = plt.subplots(figsize=(10,6))
            
            
            # unique_energies = np.array([2.5, 1, 0.25])
            # for energy in unique_energies:
            #     mask = energies == energy
            #     ax1.plot(sizes[:,0][mask], t10[mask], 'o-', label=f'E={energy:.3f}')
            
            # ax1.set_xlabel("Size[0] (мм)")
            # ax1.set_ylabel("T10")
            # ax1.legend()
            # ax1.grid(True)
            # st.pyplot(fig1)
            st.header("Зависимость T10 от энергии для разных размеров")
            fig1 = go.Figure()
    
  
            energy_fit = np.linspace(min(energies), max(energies), 100)

            t_10_grid = np.array([fit_function(x, A, b) for x in energy_fit])

            size_indices = [0,1, 2, 3,4] 
            
            # df = pd.DataFrame({"energy": energies, "retention_at_t10": t10})
            fig1.add_trace(go.Scatter(
                    x=energies,
                    y=t10,  
                    mode='markers',
                    name = "Зависимость t_10 от энергии",
                    hovertemplate="Energy: %{x:.3f} МДж/кг<br>T10/Size: %{y:.2f}<extra></extra>"
            ))
            
            fig1.add_trace(go.Scatter(
                     x=energy_fit,
                    y=t_10_grid,  
                    mode='lines',
                    name="A * (1 - np.exp(-b * x))"
            ))
            fig1.update_layout(
                xaxis_title="Энергия, МДж/т",
                yaxis_title="T10 %",
                
                template="plotly_dark"
            )
            st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("Нет доступных отчетов")
    
   
    

async def get_dwt_reports():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BACKEND_URL+'/api/dwt/reports') as resp :
            resp.raise_for_status()
            return await resp.json()
            

async def get_dwt_report(report_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BACKEND_URL+f'/api/dwt/report',  params={"report_id": report_id}) as resp :
            resp.raise_for_status()
            response_data = await resp.json()
            print(response_data)
            return response_data