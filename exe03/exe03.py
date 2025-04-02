import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("💰 Simulador de Investimento com Juros Compostos")

# Entrada do valor inicial
valor_inicial = st.number_input("Valor Inicial (R$)", min_value=0.0, value=1000.0, step=100.0)

# Entrada da taxa de juros anual
taxa_juros = st.slider("Taxa de Juros Anual (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)

# Escolha do período
anos = st.selectbox("Período (em anos)", options=list(range(1, 31)), index=4)

# Calcular o crescimento ano a ano
anos_lista = list(range(anos + 1))
valores = [valor_inicial * (1 + taxa_juros / 100) ** t for t in anos_lista]

# Criar DataFrame
df = pd.DataFrame({
    "Ano": anos_lista,
    "Valor Acumulado": valores
})

# Mostrar resultado final
st.subheader("📈 Resultado Final")
st.write(f"Após {anos} anos, o valor acumulado será de **R$ {valores[-1]:,.2f}**.")

# Gráfico com Plotly
fig = px.line(df, x="Ano", y="Valor Acumulado", title="Crescimento do Investimento ao Longo do Tempo")
st.plotly_chart(fig, use_container_width=True)
