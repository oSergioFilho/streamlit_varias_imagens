import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("🌐 Informações sobre Países (via API REST Countries)")

pais = st.text_input("Digite o nome de um país (ex: Brazil, Japan, Canada):")

if pais:
    url = f"https://restcountries.com/v3.1/name/{pais}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()[0]  # pegamos só o primeiro resultado

        nome = dados.get("name", {}).get("official", "N/A")
        capital = dados.get("capital", ["N/A"])[0]
        populacao = dados.get("population", 0)
        area = dados.get("area", 0)
        moeda = list(dados.get("currencies", {}).keys())[0] if dados.get("currencies") else "N/A"
        bandeira = dados.get("flags", {}).get("png", "")

        st.subheader(f"📌 {nome}")
        st.write(f"**Capital:** {capital}")
        st.write(f"**População:** {populacao:,}")
        st.write(f"**Área:** {area:,} km²")
        st.write(f"**Moeda:** {moeda}")
        if bandeira:
            st.image(bandeira, caption="Bandeira", width=200)

        # Gráfico de barras
        df = pd.DataFrame({
            "Indicador": ["População", "Área (km²)"],
            "Valor": [populacao, area]
        })
        fig = px.bar(df, x="Indicador", y="Valor", title="Dados Demográficos")
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.error("❌ País não encontrado. Tente outro nome.")
