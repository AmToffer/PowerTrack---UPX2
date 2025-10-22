import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- Configuração da Página ---
st.set_page_config(
    page_title="PowerTrack Simulação",
    page_icon="⚡️",
    layout="wide"
)

# --- Título do Dashboard ---
st.title("⚡️ PowerTrack: Monitoramento Inteligente de Energia")
st.caption(f"Simulação em tempo real | {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# --- Simulação de Dados por CÔMODO ---
# Função para gerar dados simulados e "realistas" para cada cômodo/circuito
def simular_dados():
    
    # Circuito 1: Quarto (Ar-Condicionado + Tomadas)
    # Consumo base (TV, carregador) + pico cíclico do Ar-Condicionado
    tomadas_quarto_w = np.random.uniform(50, 150)
    ar_cond_w = 0
    if np.random.randint(0, 3) == 1: # Liga 1/3 do tempo
        ar_cond_w = np.random.uniform(1200, 1500)
    circuito_quarto_w = tomadas_quarto_w + ar_cond_w
    
    # Circuito 2: Cozinha (Geladeira + Tomadas)
    # Consumo base (Geladeira) + picos altos (Microondas, Airfryer)
    geladeira_w = np.random.uniform(80, 200) # Cíclico
    pico_cozinha_w = 0
    if np.random.randint(0, 10) == 1: # 1 chance em 10 de um pico
        pico_cozinha_w = np.random.uniform(1000, 1800)
    circuito_cozinha_w = geladeira_w + pico_cozinha_w

    # Circuito 3: Chuveiro (Dedicado)
    # Alto consumo, mas só às vezes (simula ligado/desligado)
    circuito_chuveiro_w = 0
    if np.random.randint(0, 10) == 1: # 1 chance em 10 de estar ligado
        circuito_chuveiro_w = np.random.uniform(4500, 5500)
        
    # Circuito 4: Iluminação e Tomadas (Geral)
    # Consumo da sala, outros quartos, luzes
    circuito_geral_w = np.random.uniform(200, 600)

    # Consumo Total
    total_w = circuito_quarto_w + circuito_cozinha_w + circuito_chuveiro_w + circuito_geral_w
    
    # Prepara os dados para o dataframe
    dados = {
        'Timestamp': [datetime.now()],
        'Quarto Principal (W)': [circuito_quarto_w],
        'Cozinha (W)': [circuito_cozinha_w],
        'Chuveiro (W)': [circuito_chuveiro_w],
        'Iluminação/Geral (W)': [circuito_geral_w],
        'Consumo Total (W)': [total_w]
    }
    return pd.DataFrame(dados)

# --- Inicialização do Histórico ---
# Usamos o 'session_state' do Streamlit para guardar o histórico
if 'dados_historico' not in st.session_state:
    st.session_state.dados_historico = pd.DataFrame(columns=[
        'Timestamp', 'Quarto Principal (W)', 'Cozinha (W)', 
        'Chuveiro (W)', 'Iluminação/Geral (W)', 'Consumo Total (W)'
    ])

# --- Layout do Dashboard ---
# Criamos "slots" na tela que serão atualizados em tempo real
placeholder_metricas = st.empty()
placeholder_grafico = st.empty()

# Loop de atualização em tempo real
while True:
    # 1. Obter novos dados simulados
    novos_dados = simular_dados()
    
    # 2. Atualizar o histórico
    st.session_state.dados_historico = pd.concat(
        [st.session_state.dados_historico, novos_dados], 
        ignore_index=True
    )
    # Mantém apenas os últimos 100 registros para o gráfico não ficar lotado
    st.session_state.dados_historico = st.session_state.dados_historico.tail(100)
    
    # 3. Pegar o último registro para as métricas
    dados_atuais = novos_dados.iloc[0]

    # --- Atualizar as Métricas (Consumo Atual) ---
    with placeholder_metricas.container():
        st.subheader("Consumo em Tempo Real por Cômodo/Setor")
        
        # Cria colunas para organizar as métricas
        col1, col2, col3, col4, col5 = st.columns(5)
        
        col1.metric(
            label="🔌 Consumo Total", 
            value=f"{dados_atuais['Consumo Total (W)']:.0f} W"
        )
        col2.metric(
            label="🛏️ Quarto Principal", 
            value=f"{dados_atuais['Quarto Principal (W)']:.0f} W"
        )
        col3.metric(
            label="🍳 Cozinha", 
            value=f"{dados_atuais['Cozinha (W)']:.0f} W"
        )
        col4.metric(
            label="🚿 Chuveiro", 
            value=f"{dados_atuais['Chuveiro (W)']:.0f} W"
        )
        col5.metric(
            label="💡 Iluminação/Geral", 
            value=f"{dados_atuais['Iluminação/Geral (W)']:.0f} W"
        )

    # --- Atualizar o Gráfico (Histórico) ---
    with placeholder_grafico.container():
        st.subheader("Histórico de Consumo (Últimos 5 minutos)")
        
        # Prepara dados para o gráfico
        df_grafico = st.session_state.dados_historico.melt(
            id_vars='Timestamp', 
            var_name='Circuito', 
            value_name='Consumo (W)'
        )
        
        # Filtra para não mostrar o "Consumo Total" no gráfico de linhas
        df_grafico = df_grafico[df_grafico['Circuito'] != 'Consumo Total (W)']

        # Cria o gráfico de linhas
        st.line_chart(
            df_grafico,
            x='Timestamp',
            y='Consumo (W)',
            color='Circuito' # Cria uma linha para cada circuito
        )

    # --- Atualização ---
    # Aguarda 5 segundos, conforme especificado no projeto [cite: 92]
    time.sleep(5)