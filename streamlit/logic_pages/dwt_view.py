import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
from os import getenv

BACKEND_URL = getenv("BACKEND_URL_DEV")

def dwt_view_page():
    st.title("DWT Test Results")
    
    # Получаем список доступных образцов с сервера
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

    # Выпадающий список для выбора образца
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
                # retention_at_t10 = data["retention_at_t10"]
                st.write(data)
                # Преобразуем данные в массивы для построения графика
                energies = [point["energy"] for point in data]
                retentions = [point["retention_at_t10"] for point in data]

                # Создаем график
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=energies,
                    y=retentions,
                    mode='markers+lines',
                    name='t10 vs Energy'
                ))

                # Настраиваем внешний вид графика
                fig.update_layout(
                    title="Зависимость t10 от энергии",
                    xaxis_title="Энергия (кВт⋅ч/т)",
                    yaxis_title="t10 (%)",
                    showlegend=True
                )

                # Отображаем график
                st.plotly_chart(fig, use_container_width=True)
                # Создаем DataFrame из полученных данных
                # df = pd.DataFrame(data)
                
                # # Создаем график используя Plotly
                # fig = go.Figure()
                # fig.add_trace(go.Scatter(
                #     x=df['time'],
                #     y=df['force'],
                #     mode='lines',
                #     name='Force vs Time'
                # ))
                
                # # Настраиваем внешний вид графика
                # fig.update_layout(
                #     title=f"DWT Test Results for {selected_sample}",
                #     xaxis_title="Time (s)",
                #     yaxis_title="Force (N)",
                #     showlegend=True
                # )
                
                # # Отображаем график
                # st.plotly_chart(fig, use_container_width=True)
                
            else:
                st.error(f"Не удалось получить данные для выбранного образца{response.status_code}")
        
        except Exception as e:
            st.error(f"Ошибка при получении данных: {str(e)}")