

import streamlit as st

# Configuração da página
st.set_page_config(page_title="Formulário Centralizado", page_icon="📝", layout="centered")

# Função principal
def main():
    st.title("Formulário Centralizado")
    st.write("Por favor, preencha as perguntas abaixo:")

    # Formulário
    with st.form("form"):
        pergunta_1 = st.text_input("Pergunta 1: Qual é o seu nome?")
        pergunta_2 = st.number_input("Pergunta 2: Qual é a sua idade?", min_value=0, max_value=120, step=1)
        pergunta_3 = st.radio("Pergunta 3: Qual é o seu gênero?", ["Masculino", "Feminino", "Prefiro não dizer"])
        pergunta_4 = st.selectbox("Pergunta 4: Qual é o seu estado?", ["SP", "RJ", "MG", "BA", "Outros"])
        pergunta_5 = st.text_area("Pergunta 5: Deixe seu comentário:")

        # Botão de envio
        submit_button = st.form_submit_button("Enviar")

    # Quando o formulário é enviado
    if submit_button:
        resultado = f"""
        **Resultado do Formulário:**
        - Nome: {pergunta_1}
        - Idade: {pergunta_2}
        - Gênero: {pergunta_3}
        - Estado: {pergunta_4}
        - Comentário: {pergunta_5}
        """
        st.info("Formulário enviado com sucesso!")
        st.write(resultado)

# Rodando o aplicativo
if __name__ == "__main__":
    main()
