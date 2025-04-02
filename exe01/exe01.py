import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Análise de CSV", layout="centered")

st.title("📊 Dashboard de Análise de Dados")

# Upload do arquivo
uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leitura dos dados
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Prévia dos Dados")
    st.dataframe(df.head())

    # Seleção de coluna numérica
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    if numeric_cols:
        selected_col = st.selectbox("Selecione uma coluna numérica para análise:", numeric_cols)
        
        if selected_col:
            st.subheader(f"📈 Estatísticas da Coluna: {selected_col}")
            st.write(f"Média: {df[selected_col].mean():.2f}")
            st.write(f"Mediana: {df[selected_col].median():.2f}")
            st.write(f"Desvio Padrão: {df[selected_col].std():.2f}")

            # Gráfico interativo
            st.subheader("📊 Histograma")
            fig = px.histogram(df, x=selected_col, nbins=20, title=f"Distribuição de {selected_col}")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("O CSV não contém colunas numéricas para análise.")
else:
    st.info("Por favor, envie um arquivo CSV para começar.")
