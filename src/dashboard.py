import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# --- sua conexão (verifique se bate com o que tem em process_data.py) ---
engine = create_engine('postgresql://postgres:42418214@localhost:5432/iot_db')

# --- helper para carregar e limpar as views ---
def load_data(view_name, parse_dates=None):
    # lê a view do banco
    df = pd.read_sql(f"SELECT * FROM {view_name}", engine, parse_dates=parse_dates)
    # normaliza/limpa nomes de colunas: tira espaços, pipe + sufixos, coloca em lowercase
    df.columns = (
        df.columns
          .str.strip()
          .str.lower()
          .str.replace(' ', '_')
          .str.replace(r'\s*\|\s*.*$', '', regex=True)  # remove " | editar-código" etc.
    )
    return df

st.title('Dashboard de Temperaturas IoT')

# --- Gráfico 1: Média de temperatura por dispositivo (com mapeamento) ---
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
# mapeamento legível (ajuste nomes conforme quiser)
device_names = {
    "device_1": "Sala",
    "device_2": "Cozinha",
    "device_3": "Quintal"
}
if 'device_id' in df_avg_temp.columns:
    df_avg_temp['device_id'] = df_avg_temp['device_id'].map(device_names).fillna(df_avg_temp['device_id'])
fig1 = px.bar(
    df_avg_temp.sort_values('avg_temp', ascending=False),
    x='device_id', y='avg_temp',
    labels={"device_id": "Dispositivo", "avg_temp": "Temperatura Média (°C)"}
)
st.plotly_chart(fig1)

# --- Gráfico 2: Leituras por Hora do Dia ---
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
# se hora veio como float, converte pra int; se tiver nome estranho, corrige
if 'hora' in df_leituras_hora.columns:
    df_leituras_hora['hora'] = df_leituras_hora['hora'].astype(int)
if 'contagem' in df_leituras_hora.columns:
    df_leituras_hora = df_leituras_hora.sort_values('hora')
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem',
                   labels={"hora": "Hora do Dia", "contagem": "Quantidade de Leituras"})
    st.plotly_chart(fig2)
else:
    st.warning("A view 'leituras_por_hora' não retornou a coluna esperada 'contagem'.")

# --- Gráfico 3: Temperaturas Máx e Mín por Dia ---
st.header('Temperaturas Máximas e Mínimas por Dia')
# pede parse_dates pra garantir que 'data' venha como datetime
df_temp_max_min = load_data('temp_max_min_por_dia', parse_dates=['data'])

if 'data' in df_temp_max_min.columns:
    # normaliza para meia-noite (remove horas estranhas) e ordena
    df_temp_max_min['data'] = pd.to_datetime(df_temp_max_min['data']).dt.normalize()
    df_temp_max_min = df_temp_max_min.sort_values('data')

    # plota
    fig3 = px.line(
        df_temp_max_min,
        x='data',
        y=['temp_max', 'temp_min'],
        labels={"data": "Data", "value": "Temperatura (°C)", "variable": "Tipo"}
    )
    # formata ticks do eixo X para mostrar só a data legível
    fig3.update_xaxes(tickformat="%d/%m/%Y")
    st.plotly_chart(fig3)
else:
    st.warning("A view 'temp_max_min_por_dia' não retornou a coluna esperada 'data'.")
