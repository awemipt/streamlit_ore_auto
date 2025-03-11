import numpy as np
import streamlit as st
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
            data = asyncio.run(get_dwt_report(selected['id']))
            report = data[0]["DWT_REPORT"] 

            st.write(report)
            dwt_graph_data = data[1]["DWT_GRAPH_DATA"]
            st.write(dwt_graph_data)
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
            groups = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14)]

            for group in groups:
                fig = make_subplots(
                    rows=3, 
                    cols=1, 
                    subplot_titles=[f'График {i}' for i in group],
                    vertical_spacing=0.1
                )
                
                for idx, i in enumerate(group, start=1):
                    sizes = dwt_graph_data['sizes_to_graph'][i]
                    retentions = dwt_graph_data['retentions_to_graph'][i]
                    max_size = max(sizes)
                    x_line = max_size / 10
                    
                    # Добавление основного графика
                    fig.add_trace(
                        go.Scatter(
                            x=sizes, 
                            y=retentions, 
                            mode='lines', 
                            name=f'Данные {i}'
                        ),
                        row=idx, 
                        col=1
                    )
                    
                    # Добавление вертикальной линии
                    fig.add_shape(
                        type='line',
                        x0=x_line,
                        x1=x_line,
                        y0=0,
                        y1=100,
                        yref='paper',
                        line=dict(color='red', dash='dash'),
                        row=idx,
                        col=1
                    )
                    
                    # Настройка осей
                    fig.update_yaxes(title_text='Удержание (%)', row=idx, col=1)
                    fig.update_xaxes(title_text='Размер', row=idx, col=1)
                
                # Общие настройки
                fig.update_layout(
                    height=1200,
                    width=800,
                    title_text=f'Графики {group[0]}-{group[-1]}',
                    showlegend=False
                )
                
                st.plotly_chart(fig)
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