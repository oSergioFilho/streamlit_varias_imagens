import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Exercício 2 - Filtros Interativos com Streamlit")

# 🔹 Gerar dados fictícios
np.random.seed(42)
cidades = ['Goiânia', 'São Paulo', 'Curitiba', 'Rio de Janeiro', 'Salvador']
categorias = ['Alimentos', 'Eletrônicos', 'Roupas', 'Brinquedos']

dados = pd.DataFrame({
    'Cidade': np.random.choice(cidades, 200),
    'Categoria': np.random.choice(categorias, 200),
    'Valor': np.random.randint(50, 1000, size=200)
})

st.subheader("🔍 Filtros")

# 🔸 Filtro por cidade
cidades_selecionadas = st.multiselect(
    "Filtrar por cidade:",
    options=sorted(dados['Cidade'].unique()),
    default=sorted(dados['Cidade'].unique())
)

# 🔸 Filtro por categoria
categorias_selecionadas = st.multiselect(
    "Filtrar por categoria:",
    options=sorted(dados['Categoria'].unique()),
    default=sorted(dados['Categoria'].unique())
)

# 🔸 Filtro por faixa de valor
valor_min = int(dados['Valor'].min())
valor_max = int(dados['Valor'].max())
faixa_valor = st.slider(
    "Filtrar por faixa de valor (R$):",
    min_value=valor_min,
    max_value=valor_max,
    value=(valor_min, valor_max)
)

# 🔹 Aplicar filtros
dados_filtrados = dados[
    (dados['Cidade'].isin(cidades_selecionadas)) &
    (dados['Categoria'].isin(categorias_selecionadas)) &
    (dados['Valor'] >= faixa_valor[0]) &
    (dados['Valor'] <= faixa_valor[1])
]

st.subheader("📋 Dados Filtrados")
st.write(f"{dados_filtrados.shape[0]} registros encontrados.")
st.dataframe(dados_filtrados)
