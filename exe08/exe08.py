import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.title("📈 Previsão de Notas com Regressão Linear")

# 🔹 Dados de exemplo: Horas de estudo vs. Nota final
np.random.seed(42)
horas_estudo = np.random.uniform(1, 10, 50).reshape(-1, 1)
notas = (horas_estudo * 10 + np.random.normal(0, 5, (50, 1))).reshape(-1)

# 🔹 Treinar o modelo
modelo = LinearRegression()
modelo.fit(horas_estudo, notas)

# 🔸 Entrada do usuário
horas = st.slider("Quantas horas você estudou?", min_value=1, max_value=10, value=5)
nota_prevista = modelo.predict(np.array([[horas]]))[0]

st.subheader("🔮 Previsão")
st.write(f"Se você estudar por **{horas} horas**, a nota prevista é **{nota_prevista:.2f}**")

# 🔸 Gráfico comparando os dados e a previsão
df = pd.DataFrame({
    "Horas de Estudo": horas_estudo.flatten(),
    "Notas Reais": notas
})

df_novo = pd.DataFrame({
    "Horas de Estudo": [horas],
    "Notas Reais": [nota_prevista]
})

st.subheader("📊 Comparação com os dados existentes")
fig = px.scatter(df, x="Horas de Estudo", y="Notas Reais", title="Notas x Horas de Estudo")
fig.add_scatter(x=df_novo["Horas de Estudo"], y=df_novo["Notas Reais"], mode="markers", marker=dict(size=12, color='red'), name="Sua previsão")
st.plotly_chart(fig, use_container_width=True)
