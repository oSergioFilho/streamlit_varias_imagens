import streamlit as st
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

st.title("🧠 Análise de Texto com Nuvem de Palavras")

# Entrada do usuário
texto = st.text_area("Digite ou cole seu texto aqui:")

if texto.strip():
    # Limpeza simples e separação
    palavras = texto.lower().split()
    contagem = Counter(palavras)

    # Estatísticas básicas
    num_palavras = len(palavras)
    num_caracteres = len(texto)

    st.subheader("📊 Estatísticas do Texto")
    st.write(f"**Palavras:** {num_palavras}")
    st.write(f"**Caracteres:** {num_caracteres}")

    # Top 5 palavras mais frequentes
    st.subheader("🔝 5 Palavras Mais Frequentes")
    top5 = contagem.most_common(5)
    for palavra, freq in top5:
        st.write(f"• **{palavra}**: {freq}x")

    # Nuvem de palavras
    st.subheader("☁️ Nuvem de Palavras")
    wc = WordCloud(width=800, height=300, background_color="white").generate(texto)

    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

else:
    st.info("✍️ Digite um texto acima para iniciar a análise.")
