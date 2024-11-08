# Importa as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import Graphics_Functions as graf
import base64
import matplotlib

matplotlib.use('Agg')

# Função para converter imagem para Base64
def img_to_base64(caminho_imagem: str) -> str:
    """
    Converte uma imagem para uma string codificada em Base64.

    Args:
    caminho_imagem (str): Caminho completo para o arquivo da imagem.

    Returns:
    str: String da imagem codificada em Base64.
    """
    with open(caminho_imagem, "rb") as img_file:
        # Lê a imagem e codifica em Base64
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded_string

# Caminhos das imagens e conversão para Base64
img1 = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\one-bit_logo.png"
img1 = img_to_base64(img1)

img2 = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\Spotify_logo.png"
img2 = img_to_base64(img2)

img3 = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\youtube_logo.png"
img3 = img_to_base64(img3)

img4 = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\Algoritmo_personalizado.png"
img4 = img_to_base64(img4)

# HTML para a exibição do logo Onebit
onebit_logo = f"""
    <div style="text-align: center; padding: 20px;">
        <img src="data:image/png;base64,{img1}"
            style="width: 100%; border-radius: 10px; box-shadow: 5px 5px 15px rgba(0,0,0,0.3);"
            alt="Logo da 1-Bit">
    </div>
"""

# Leitura do dataset e pré-processamento
df = pd.read_csv(r'C:\Users\reis_\Downloads\music_streaming.csv')
df['date'], df['time'] = pd.to_datetime(df['date'], format='%Y-%m-%d'), pd.to_datetime(df['time'], format='%H:%M:%S')
df['month'], df['hour'] = df['date'].dt.month, df['time'].dt.hour
df = df.drop_duplicates(subset='user_id')  # Remove registros duplicados com o mesmo user_id

# Inicialização do estado das variáveis
if 'show_horariospico' not in st.session_state:
    st.session_state.show_horariospico = False
if 'show_genres' not in st.session_state:
    st.session_state.show_genres = False
if 'show_subgenres' not in st.session_state:
    st.session_state.show_subgenres = False
if 'show_liked' not in st.session_state:
    st.session_state.show_liked = False
if 'show_streamquality' not in st.session_state:
    st.session_state.show_streamquality = False
if 'show_subtype' not in st.session_state:
    st.session_state.show_subtype = False
if 'show_platf' not in st.session_state:
    st.session_state.show_platf = False
if 'show_month' not in st.session_state:
    st.session_state.show_month = False
if 'show_comp_idade_genre' not in st.session_state:
    st.session_state.show_comp_age_genre = False
if 'show_comp_onl_age' not in st.session_state:
    st.session_state.show_comp_onl_age = False

# Funções para controlar a exibição dos gráficos
def toggle_horariospico():
    st.session_state.show_horariospico = not st.session_state.show_horariospico
def toggle_genres():
    st.session_state.show_genres = not st.session_state.show_genres
def toggle_subgenres():
    st.session_state.show_subgenres = not st.session_state.show_subgenres
def toggle_liked():
    st.session_state.show_liked = not st.session_state.show_liked
def toggle_streamquality():
    st.session_state.show_streamquality = not st.session_state.show_streamquality
def toggle_subtype():
    st.session_state.show_subtype = not st.session_state.show_subtype
def toggle_platf():
    st.session_state.show_platf = not st.session_state.show_platf
def toggle_month():
    st.session_state.show_month = not st.session_state.show_month
def toggle_heatmap():
    st.session_state.show_comp_age_genre = not st.session_state.show_comp_age_genre
def toggle_heatmap2():
    st.session_state.show_comp_onl_age = not st.session_state.show_comp_onl_age 

# Criação da barra lateral no Streamlit
st.sidebar.markdown(onebit_logo, unsafe_allow_html=True)  # Exibe o logo Onebit
st.sidebar.title('Central de comando')
menu = st.sidebar.radio("Escolha uma opção", ('Introdução', 'Gráficos do Dataset', 'Solução'))

# Se o usuário escolheu a opção 'Introdução'
if menu == 'Introdução':
    st.title('Bem-vindo ao Dashboard do Streaming de Música!')
    st.markdown("""
        <h4 style="font-size: 25px; text-align: justify;">
            Somos alunos do Novo Ensino Suplementar (NES). Este trabalho é destinado à matéria de Prática e Pesquisa. 
            A pesquisa se baseia no Data Shark, e nosso foco é analisar o dataset de Streaming de Música, com a criação de gráficos usando a biblioteca matplotlib.
        </h4>""", unsafe_allow_html=True)

    st.markdown("""<h4 style="font-size: 25px; text-align: justify;">
            Através dessa análise, buscamos identificar problemas ou oportunidades no comportamento de usuários no streaming de música.
            As análises incluem aspectos como análise temporal, distribuição, relacionamentos e categorias. 
            Essas análises ajudaram a identificar áreas de melhoria.
        </h4>""", unsafe_allow_html=True)

# Se o usuário escolheu a opção 'Gráficos do Dataset'
elif menu == 'Gráficos do Dataset':
    st.title('Gráficos!')

    col1, col2 = st.columns(2)

    # Botões para ativar gráficos
    with col1:
        if st.button('Horários de Pico'):
            toggle_horariospico()
        if st.button("Gêneros Escutados"):
            toggle_genres()
        if st.button("Subgêneros Escutados"):
            toggle_subgenres()
        if st.button("Likes nas Reproduções"):
            toggle_liked()
        if st.button("Qualidade de Stream"):
            toggle_streamquality()
    with col2:
        if st.button('Tipos de Assinaturas'):
            toggle_subtype()
        if st.button('Plataformas Usadas'):
            toggle_platf()
        if st.button("Quantidade de Reproduções por Mês"):
            toggle_month()
        if st.button("Comparação entre Idade e Gênero Escutado"):
            toggle_heatmap()
        if st.button("Comparação entre Estado de Wifi e Idade"):
            toggle_heatmap2()

    # Exibe os gráficos conforme o estado de cada variável
    if st.session_state.show_horariospico:
        graf.show_picos_idade()
    if st.session_state.show_genres:
        graf.show_genres()
    if st.session_state.show_subgenres:
        graf.show_subgenres()
    if st.session_state.show_liked:
        graf.show_liked()
    if st.session_state.show_streamquality:
        graf.show_streamqual()
    if st.session_state.show_subtype:
        graf.show_subtypes()
    if st.session_state.show_platf:
        graf.show_platf()
    if st.session_state.show_month:
        graf.show_month()
    if st.session_state.show_comp_age_genre:
        graf.show_comp1()
    if st.session_state.show_comp_onl_age:
        graf.show_comp2()

# Se o usuário escolheu a opção 'Solução'
elif menu == 'Solução':
    st.title("A Solução")
    
    # Descrição da solução com formatação adequada
    st.markdown(""" 
        <h4 style="font-size: 25px; text-align: justify;">
            Para resolver o problema das recomendações, podemos analisar como grandes empresas como o Spotify e Youtube lidam com isso.
        </h4>
    """, unsafe_allow_html=True)
    
    # Colunas para exibir título e imagem lado a lado
    col1, col2 = st.columns([1, 3])
    
    # Exibindo o título "Spotify" e a imagem
    with col1:
        st.markdown(""" 
            <h2 style="font-size: 40px; text-align: left;">
                Spotify
            </h2>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="text-align: center; margin-left: -200px;">
            <img src="data:image/png;base64,{img2}"
                 style="width: 20%; max-width: 150px; border-radius: 10px; box-shadow: 5px 5px 15px rgba(0,0,0,0.3);"
                 alt="Logo do Spotify">
        </div>
        """, unsafe_allow_html=True)
    
    # Explicação sobre o algoritmo do Spotify
    st.markdown(""" 
        <h4 style="font-size: 25px; text-align: justify;">
            O algoritmo do Spotify usa o histórico de audição dos usuários, como o humor, gênero e estilo musical mais consumidos, para fazer recomendações mais precisas.
        </h4>
    """, unsafe_allow_html=True)

    # Colunas para exibir título e imagem do Youtube
    col3, col4 = st.columns([1, 3])
    with col3:
        st.markdown("""
            <h2 style="font-size: 40px; text-align: left;">
                Youtube
            </h2>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div style="text-align: center; margin-left: -200px;">
            <img src="data:image/png;base64,{img3}"
                 style="width: 16%; max-width: 150px; border-radius: 10px; box-shadow: 5px 5px 15px rgba(0,0,0,0.3);"
                 alt="Logo do Youtube">
        </div>
        """, unsafe_allow_html=True)
    
    # Explicação sobre o algoritmo do Youtube
    st.markdown(""" 
        <h4 style="font-size: 25px; text-align: justify;">
            O algoritmo do Youtube usa o histórico de visualizações, priorizando vídeos com maior popularidade e visualizações, para recomendar novos conteúdos aos usuários.
        </h4>""", unsafe_allow_html=True)

    # Descrição da solução proposta
    st.markdown(""" 
        <h2 style="font-size: 40px; text-align: left;">
            Nossa Solução
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown(""" 
        <h4 style="font-size: 25px; text-align: justify;">
            Analisamos o dataset e identificamos que a taxa de curtidas era muito baixa. Nossa solução envolve um algoritmo personalizado, 
            combinando os métodos de histórico de audição do Spotify com o histórico de visualizações do Youtube.
        </h4>
    """, unsafe_allow_html=True)

    # Exibe o diagrama do algoritmo personalizado
    st.markdown(f"""
    <div style='text-align: center; padding-top: 40px;'>
        <img src='data:image/png;base64,{img4}'
            style='width: 100%; max-width: 600px; border-radius: 5px; box-shadow: 10px 10px 20px rgba(0,0,0,0.5);'
            alt='Diagrama do algoritmo personalizado'>
    </div>
""", unsafe_allow_html=True)
