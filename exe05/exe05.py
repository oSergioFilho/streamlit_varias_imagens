import streamlit as st

st.title("📝 Formulário com Validação e Resultados")

# Contêiner do formulário
with st.form(key="formulario"):
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    cores = st.multiselect("Selecione suas cores preferidas:", ["Azul", "Verde", "Vermelho", "Amarelo", "Preto", "Branco"])

    enviar = st.form_submit_button("Enviar")
    limpar = st.form_submit_button("Limpar")

# Lógica para submissão
if enviar:
    if nome.strip() == "":
        st.warning("⚠️ Por favor, preencha seu nome.")
    elif not (0 <= idade <= 120):
        st.warning("⚠️ Idade fora do intervalo permitido.")
    elif not cores:
        st.warning("⚠️ Selecione ao menos uma cor.")
    else:
        cores_formatadas = ", ".join(cores)
        st.success(f"👋 Olá, **{nome}**, com **{idade}** anos, você gosta de **{cores_formatadas}**!")

# "Limpar" é simbólico, já que Streamlit não tem reset real
if limpar:
    st.rerun()

