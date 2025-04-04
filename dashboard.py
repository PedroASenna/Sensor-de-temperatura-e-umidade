import streamlit as st
import random
import time
import pandas as pd
import plotly.express as px
from datetime import datetime

# Configuração da página (tema escuro, layout amplo)
st.set_page_config(
    page_title="🌡️ Dashboard de Sensores Avançado",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para melhorar o visual
st.markdown("""
<style>
    .stMetricLabel { font-weight: bold !important; }
    .st-b7 { color: #FF4B4B !important; }  /* Cor para alertas */
    .css-1aumxhk { background-color: #0E1117; }  /* Fundo escuro */
</style>
""", unsafe_allow_html=True)

# Título com estilo
st.title("📊 Dashboard de Monitoramento")
st.markdown("---")

# Função para simular leituras realistas (umidade e temperatura correlacionadas)
def ler_sensor():
    base_temp = random.uniform(20.0, 30.0)
    temperatura = round(base_temp + random.gauss(0, 0.5), 1)
    umidade = round(80 - (base_temp - 20) * 1.5 + random.gauss(0, 3), 1)
    return max(15.0, temperatura), max(30.0, min(100.0, umidade))

# Sidebar para controles
with st.sidebar:
    st.header("⚙️ Controles")
    intervalo = st.slider("Intervalo de atualização (segundos)", 1, 10, 2)
    limite_temp = st.slider("Alerta de Temperatura (°C)", 25, 35, 28)
    limite_umid = st.slider("Alerta de Umidade (%)", 70, 90, 80)

# Inicializar dados
if 'dados' not in st.session_state:
    st.session_state.dados = pd.DataFrame(columns=['Timestamp', 'Temperatura', 'Umidade'])

# Layout em colunas para métricas
col1, col2, col3 = st.columns(3)
ultima_atualizacao = col3.empty()  # Para mostrar o horário da última leitura

# Placeholders para gráficos
graf_temp = st.empty()
graf_umid = st.empty()

# Loop de atualização
while True:
    temp, umid = ler_sensor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Adicionar novos dados (mantendo histórico das últimas 50 leituras)
    new_data = pd.DataFrame([[timestamp, temp, umid]], columns=['Timestamp', 'Temperatura', 'Umidade'])
    st.session_state.dados = pd.concat([st.session_state.dados, new_data]).tail(50)
    
    # Métricas com alertas visuais
    with col1:
        st.metric("🌡️ Temperatura Atual", 
                f"{temp} °C",
                delta=f"{st.session_state.dados['Temperatura'].iloc[-1] - st.session_state.dados['Temperatura'].iloc[-2]:.1f} °C" if len(st.session_state.dados) > 1 else "",
                delta_color="inverse" if temp > limite_temp else "normal")
    
    with col2:
        st.metric("💧 Umidade Atual", 
                f"{umid}%",
                delta=f"{st.session_state.dados['Umidade'].iloc[-1] - st.session_state.dados['Umidade'].iloc[-2]:.1f}%" if len(st.session_state.dados) > 1 else "",
                delta_color="inverse" if umid > limite_umid else "normal")
    
    ultima_atualizacao.caption(f"🕒 Última atualização: {timestamp}")
    
    # Gráficos animados com Plotly
    fig_temp = px.line(
        st.session_state.dados, 
        x='Timestamp', 
        y='Temperatura',
        title='📈 Variação de Temperatura',
        template='plotly_dark',
        range_y=[15, 35],
        color_discrete_sequence=["#FF4B4B"]
    ).update_layout(yaxis_title="°C", xaxis_title="Tempo")

    fig_umid = px.line(
        st.session_state.dados, 
        x='Timestamp', 
        y='Umidade',
        title='📉 Variação de Umidade',
        template='plotly_dark',
        range_y=[30, 100],
        color_discrete_sequence=["#00CC96"]
    ).update_layout(yaxis_title="%", xaxis_title="Tempo")
    
    # Exibir gráficos
    graf_temp.plotly_chart(fig_temp, use_container_width=True)
    graf_umid.plotly_chart(fig_umid, use_container_width=True)
    
    time.sleep(intervalo)  # Intervalo configurável