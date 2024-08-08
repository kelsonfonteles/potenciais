

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Função para gerar números de celular fictícios com o padrão especificado
def gerar_celular(index):
    prefixos = ['(85)9-99', '(85)9-98']
    prefixo = np.random.choice(prefixos)
    sufixo = np.random.randint(10, 100)  # Número entre 10 e 99
    return f'{prefixo}{sufixo:02}'

# Lista de dados fornecida com uma coluna adicional de Celular
dados = [
    {"Nome": "Manuel Costa", "Título": "Líder da obra missionária", "Local": "Palmeiras", "Votos": 380},
    {"Nome": "Renato Cardoso", "Título": "Liderança Região", "Local": "Jangurussu", "Votos": 120},
    {"Nome": "Bispo Marcos", "Título": "Bispo", "Local": "Ala Cidade dos Funcionários", "Votos": 75},
    {"Nome": "Bispo Mesquita", "Título": "Bispo", "Local": "Ala Eusebio", "Votos": 83},
    {"Nome": "Lean Paupina", "Título": "Bispo", "Local": "Ala Paupina", "Votos": 90},
    {"Nome": "Prof Júlio César", "Título": "Bispo", "Local": "Ala Messejana", "Votos": 180},
    {"Nome": "Frederick Pouchant", "Título": "Presidente da Estaca", "Local": "Messejana II", "Votos": 240},
    {"Nome": "Kelson Fonteles", "Título": "Secretário de Informação da Igreja", "Local": "Washington Soares", "Votos": 325},
    {"Nome": "João Evandro", "Título": "Coordenador da obra missionária", "Local": "Ala Barroso", "Votos": 140},
    {"Nome": "Ana Cristina Barbosa", "Título": "Sociedade Socorro", "Local": "Palmeira I e II", "Votos": 190},
    {"Nome": "Bispo Helder", "Título": "Bispo", "Local": "Ala José Walter", "Votos": 120},
    {"Nome": "Bispo Assunção", "Título": "Bispo", "Local": "Ala Lagoa Redonda", "Votos": 90},
    {"Nome": "Enfermeira Tatiane", "Título": "Coodenadora do Ambulatório de Coagulopatias Hemoce", "Local": "Montese", "Votos": 75},
    {"Nome": "Maquine Souza Pedras", "Título": "Presidente do Ramo", "Local": "Alamedas", "Votos": 85},
    {"Nome": "Ana Claudia", "Título": "Líder na Sociedade de Socorro", "Local": "Guajerú", "Votos": 60},
    {"Nome": "Francisco do Galetão", "Título": "Líder Comunitário", "Local": "Sapiranga", "Votos": 73},
    {"Nome": "Romoaldo Batista", "Título": "Presidente do Quórum de Élderes", "Local": "Ala Alvorada", "Votos": 42},
    {"Nome": "Maria do Carmo", "Título": "Coordenadora de Projetos Sociais", "Local": "Parque Dois Irmãos", "Votos": 65},
    {"Nome": "João Batista", "Título": "Presidente da Associação Comunitária", "Local": "Messejana", "Votos": 78},
    {"Nome": "Sandra Silva", "Título": "Líder Comunitária", "Local": "Parangaba", "Votos": 50},
    {"Nome": "Paulo Nogueira", "Título": "Coordenador de Atividades Culturais", "Local": "Barra do Ceará", "Votos": 85},
    {"Nome": "Patrícia Almeida", "Título": "Supervisora de Educação", "Local": "Aldeota", "Votos": 70},
    {"Nome": "Carlos Eduardo", "Título": "Responsável pela Segurança Comunitária", "Local": "Conjunto Ceará", "Votos": 55}
]

# Adicionando números de celular fictícios com o padrão correto
for i, item in enumerate(dados):
    item["Celular"] = gerar_celular(i)

# Convertendo a lista de dicionários em um DataFrame
df = pd.DataFrame(dados)

# Calculando o total de votos
total_votos = df['Votos'].sum()

# Configurando o layout do Streamlit
st.title("Dados dos Líderes e Coordenadores")

# Exibindo o card com o total de votos
st.write("### Total de Votos Potenciais:")
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
        <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); width: 50%;">
            <h2 style="color: black; text-align: center;">Total de Votos Potenciais: {total_votos}</h2>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Configurando o gráfico
st.write("### Gráfico de Votos por Local")

# Criando o gráfico de barras horizontais
fig, ax = plt.subplots(figsize=(12, 8))
df_sorted = df.sort_values(by='Votos', ascending=True)  # Ordenar para melhor visualização
bars = ax.barh(df_sorted['Local'], df_sorted['Votos'], color='skyblue', edgecolor='grey')

# Adicionando rótulos com os valores na ponta das barras
for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{width}', va='center')

# Suavizando o gráfico
ax.set_xlabel('Votos')
ax.set_ylabel('Local')
ax.set_title('Votos por Local')
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Exibindo o gráfico no Streamlit
st.pyplot(fig)

# Exibindo a tabela com os dados
st.write("### Tabela de Dados")
st.dataframe(df.style.set_properties(**{'max-width': '100%', 'overflow-x': 'auto'}))
