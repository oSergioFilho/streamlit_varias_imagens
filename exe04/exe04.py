import streamlit as st
import pandas as pd
import numpy as np

st.title("🗺️ Mapa Interativo com Filtros")

# 🔹 Gerar dados fictícios
np.random.seed(42)
categorias = ['Evento', 'Cidade', 'Ponto Turístico']
dados = pd.DataFrame({
    'Categoria': np.random.choice(categorias, 100),
    'Latitude': np.random.uniform(-23.6, -15.5, 100),   # Região Brasil
    'Longitude': np.random.uniform(-48.0, -40.0, 100)
})

# 🔸 Filtro por categoria
categoria_selecionada = st.selectbox("Filtrar por categoria:", sorted(dados['Categoria'].unique()))

# 🔹 Filtrar dados
dados_filtrados = dados[dados['Categoria'] == categoria_selecionada]

# 🔸 Mostrar mapa com os pontos filtrados
st.subheader("🌍 Mapa de Localizações")

# ✅ Corrigir nomes das colunas para 'latitude' e 'longitude'
dados_filtrados = dados_filtrados.rename(columns={"Latitude": "latitude", "Longitude": "longitude"})

# Mostrar mapa
st.map(dados_filtrados[['latitude', 'longitude']])