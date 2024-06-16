import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    # Configuración de la página debe ser la primera instrucción
    st.set_page_config(page_title="Economic Indicators Dashboard", layout="wide")
    
    IPC = pd.read_excel('Indicadores.xlsx', sheet_name='IPC Var Interanual')

    EMBI = pd.read_excel('Indicadores.xlsx', sheet_name='EMBI')


    # Ajustar el formato de fechas en IPC y renombrar columna si es necesario
    if 'Fechas' in IPC.columns or 'Unnamed: 0' in IPC.columns:
        IPC.rename(columns={'Unnamed: 0': 'Fechas'}, inplace=True)
        IPC['Fechas'] = pd.to_datetime(IPC['Fechas'], errors='coerce')
        IPC = IPC.dropna(subset=['Fechas'])
    else:
        st.error("La hoja 'IPC Var Interanual' no contiene la columna 'Fechas'.")


    # Sección IPC
    st.header("Seleccione el rango de fechas para IPC")
    if 'Fechas' in IPC.columns:
        start_date_IPC = st.date_input("Fecha de inicio IPC", value=IPC['Fechas'].min(), key='IPC_start_date')
        end_date_IPC = st.date_input("Fecha de fin IPC", value=IPC['Fechas'].max(), key='IPC_end_date')

        # ¡Aquí se arregla el problema!
        from datetime import datetime, date
        start_date_IPC = datetime.combine(start_date_IPC, datetime.min.time())
        end_date_IPC = datetime.combine(end_date_IPC, datetime.min.time())

        IPC_filtered = IPC[(IPC['Fechas'] >= start_date_IPC) & (IPC['Fechas'] <= end_date_IPC)]

        st.header("Indice de Precios al Consumidor, Variacion Interanual a Nivel C.A. 2014 a 2024")
        st.subheader("2014 a 2024, Países de Centroamérica")
        # Gráfico específico tipo línea para IPC y sus componentes
        fig = go.Figure()
        # Corrección para manejar columnas no numéricas
        IPC_filtered = IPC_filtered.loc[:, ~IPC_filtered.columns.str.contains('^Unnamed')]
        for column in IPC_filtered.columns[1:]:
            # Convertir la columna a numérica, reemplazando valores no numéricos con NaN
            IPC_filtered[column] = pd.to_numeric(IPC_filtered[column], errors='coerce')
            fig.add_trace(go.Scatter(x=IPC_filtered['Fechas'], y=IPC_filtered[column], mode='lines', name=column))
        #fig.update_layout(title='IPC y sus componentes a lo largo del tiempo', xaxis_title='Fecha', yaxis_title='Valor', legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("La hoja 'El Salvador (IPC)' no contiene la columna 'Fechas'.")






    # Ajustar el formato de fechas en EMBI y renombrar columna si es necesario
    if 'Fecha' in EMBI.columns or 'Unnamed: 0' in EMBI.columns:
        EMBI.rename(columns={'Unnamed: 0': 'Fecha'}, inplace=True)
        EMBI['Fecha'] = pd.to_datetime(EMBI['Fecha'], errors='coerce')
        EMBI = EMBI.dropna(subset=['Fecha'])
    else:
        st.error("La hoja 'EMBI' no contiene la columna 'Fechas'.")


    # Sección EMBI
    st.header("Seleccione el rango de fechas para EMBI")
    if 'Fecha' in EMBI.columns:
        start_date_EMBI = st.date_input("Fecha de inicio EMBI", value=EMBI['Fecha'].min(), key='EMBI_start_date')
        end_date_EMBI = st.date_input("Fecha de fin EMBI", value=EMBI['Fecha'].max(), key='EMBI_end_date')

        # ¡Aquí se arregla el problema!
        from datetime import datetime, date
        start_date_EMBI = datetime.combine(start_date_EMBI, datetime.min.time())
        end_date_EMBI = datetime.combine(end_date_EMBI, datetime.min.time())

        EMBI_filtered = EMBI[(EMBI['Fecha'] >= start_date_EMBI) & (EMBI['Fecha'] <= end_date_EMBI)]

        st.header("Indice de Precios al Consumidor, Variacion Interanual a Nivel C.A. 2014 a 2024")
        st.subheader("2014 a 2024, Países de Centroamérica")
        # Gráfico específico tipo línea para EMBI y sus componentes
        fig = go.Figure()
        # Corrección para manejar columnas no numéricas
        EMBI_filtered = EMBI_filtered.loc[:, ~EMBI_filtered.columns.str.contains('^Unnamed')]
        for column in EMBI_filtered.columns[1:]:
            # Convertir la columna a numérica, reemplazando valores no numéricos con NaN
            EMBI_filtered[column] = pd.to_numeric(EMBI_filtered[column], errors='coerce')
            fig.add_trace(go.Scatter(x=EMBI_filtered['Fecha'], y=EMBI_filtered[column], mode='lines', name=column))
        #fig.update_layout(title='EMBI y sus componentes a lo largo del tiempo', xaxis_title='Fecha', yaxis_title='Valor', legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("La hoja 'El Salvador (EMBI)' no contiene la columna 'Fechas'.")



if __name__ == "__main__":
    main()
