import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎬 Sistema de Recomendação de Filmes")

# Preferências do usuário
generos_disponiveis = ["Ação", "Comédia", "Drama", "Ficção Científica", "Romance", "Terror"]
generos_selecionados = st.multiselect("Escolha seus gêneros favoritos:", generos_disponiveis)

# Banco de filmes (hardcoded)
filmes = [
    {"nome": "Missão Impossível", "gênero": "Ação"},
    {"nome": "Todo Mundo em Pânico", "gênero": "Comédia"},
    {"nome": "Interestelar", "gênero": "Ficção Científica"},
    {"nome": "Titanic", "gênero": "Romance"},
    {"nome": "Corra!", "gênero": "Terror"},
    {"nome": "O Poderoso Chefão", "gênero": "Drama"},
    {"nome": "De Volta para o Futuro", "gênero": "Ficção Científica"},
    {"nome": "Uma Linda Mulher", "gênero": "Romance"},
    {"nome": "Coringa", "gênero": "Drama"},
    {"nome": "Velozes e Furiosos", "gênero": "Ação"}
]

# Cálculo simples de pontuação
df = pd.DataFrame(filmes)
df["pontuacao"] = df["gênero"].apply(lambda g: 10 if g in generos_selecionados else 2)
df_ordenado = df.sort_values(by="pontuacao", ascending=False)

# Exibição
st.subheader("🎯 Recomendações Baseadas nas Suas Preferências")
for _, row in df_ordenado.iterrows():
    st.write(f"{row['nome']} — {row['gênero']} (Pontuação: {row['pontuacao']})")

# Gráfico
st.subheader("📊 Pontuação das Recomendações")
fig = px.bar(df_ordenado, x="nome", y="pontuacao", color="gênero", title="Pontuação por Filme")
st.plotly_chart(fig, use_container_width=True)
