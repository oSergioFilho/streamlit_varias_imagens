import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="App Multi-Página", layout="wide")

st.sidebar.title("📂 Navegação")
pagina = st.sidebar.radio("Ir para:", ["📁 Página 1 - Upload", "📊 Página 2 - Estatísticas", "📈 Página 3 - Gráficos"])

# 🔸 Página 1: Upload
if pagina.startswith("📁"):
    st.title("📁 Página 1 - Upload de Dados")

    arquivo = st.file_uploader("Faça o upload de um arquivo CSV", type=["csv"])

    if arquivo is not None:
        df = pd.read_csv(arquivo)
        st.session_state["dados"] = df
        st.success("✅ Dados carregados com sucesso!")
        st.dataframe(df)

# 🔸 Página 2: Estatísticas
elif pagina.startswith("📊"):
    st.title("📊 Página 2 - Análise Estatística")

    if "dados" in st.session_state:
        df = st.session_state["dados"]

        @st.cache_data
        def resumo_estatistico(data):
            return data.describe()

        st.subheader("Resumo estatístico")
        st.write(resumo_estatistico(df))
    else:
        st.warning("⚠️ Nenhum dado carregado. Vá para a Página 1 e carregue um CSV.")

# 🔸 Página 3: Gráficos
elif pagina.startswith("📈"):
    st.title("📈 Página 3 - Gráficos Interativos")

    if "dados" in st.session_state:
        df = st.session_state["dados"]
        colunas_numericas = df.select_dtypes(include="number").columns.tolist()

        if colunas_numericas:
            x_col = st.selectbox("Selecione a coluna X", colunas_numericas)
            y_col = st.selectbox("Selecione a coluna Y", colunas_numericas)

            fig = px.scatter(df, x=x_col, y=y_col, title="Gráfico de Dispersão")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ Nenhuma coluna numérica encontrada no dataset.")
    else:
        st.warning("⚠️ Nenhum dado carregado. Vá para a Página 1 e carregue um CSV.")
