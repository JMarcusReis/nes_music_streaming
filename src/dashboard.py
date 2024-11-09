# Importa as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import Graphics_Functions as graf
import base64

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

Joao = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\JoaoM.png"
Joao = img_to_base64(Joao)

Gustavo = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\Gustavo.png"
Gustavo = img_to_base64(Gustavo)

Ruan = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\Ruan.png"
Ruan = img_to_base64(Ruan)

Lorena = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\Lorena.png"
Lorena = img_to_base64(Lorena)

Rodrigo = r"C:\Users\reis_\Desktop\Codes\.vscode\Python\NES\P_P\Trabalho_1\nes_music_streaming\src\assets\Rodrigo.png"
Rodrigo = img_to_base64(Rodrigo)

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

# Inicialização do estado das variáveis
if 'selected_graph' not in st.session_state:
    st.session_state.selected_graph = 'Introdução'

# Criação da barra lateral no Streamlit
st.sidebar.markdown(onebit_logo, unsafe_allow_html=True)  # Exibe o logo Onebit
st.sidebar.title('Central de comando')

# Opções de gráficos
graph_options = [
    'Introdução',
    'Análise temporal',
    'Análise de Distribuição',
    'Análise de Relacionamento',
    'Análise Categórica',
    'Solução',
    'Informações sobre o grupo'
]

# Seleção do gráfico na barra lateral
atual = st.sidebar.selectbox('Escolha uma opção', graph_options)
st.session_state.selected_graph = atual

# Se o usuário escolheu a opção 'Introdução'
if atual == 'Introdução':
    st.title('Bem-vindo ao Dashboard do Streaming de Música!')
    st.markdown("""<h4 style="font-size: 25px; text-align: justify;">
            O mundo atual em que vivemos está em constante mudança,  agora, não é mais necessário que uma pessoa fique 
            olhando a programação de um canal, pois os serviços de streaming permitem que ela assista quando e onde quiser. 
            O mesmo vale para as rádios, onde as pessoas não precisam ficar ouvindo as músicas das quais não gostam, 
            pois basta colocar sua música preferida para tocar.
        </h4>""", unsafe_allow_html=True)

    st.markdown("""<h4 style="font-size: 25px; text-align: justify;">
            Assim, criamos nossa própria “ponte”, que facilita com que a pessoa não se 
            preocupe com músicas das quais não gosta em nosso streaming, e assim ela pode aproveitar o seu momento de lazer 
            sem problemas. Pensando nisso, visando a obtenção de melhores resultados de recomendação, o grupo 1-Bit, 
            busca a excelência em resultados de plataformas de streaming de música idealizou o Algoritmo Personalizado.
        </h4>""", unsafe_allow_html=True)

# Se o usuário escolheu qualquer gráfico do dataset
elif atual == 'Análise temporal':
    # Título da Análise Temporal
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Análise Temporal</h2>
    """, unsafe_allow_html=True)
    
    # Introdução
    st.markdown("""
        <h4 style='font-size: 25px; text-align: justify;'>
            Com a análise temos os seguintes gráficos sobre análise temporal:
        </h4>
    """, unsafe_allow_html=True)
    
    # Gráfico de Horários de pico de visualizações
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">
            Horários de pico de visualizações
        </h2>
    """, unsafe_allow_html=True)
    graf.show_picos_idade()  # Chama a função para exibir o gráfico de horários
    
    # Observações sobre os horários de pico
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        Horários com mais visualizações:
        1) 22h
        2) 21h
        3) 17h
    """)
    st.markdown("---")
    
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Frequência de reproduções por mês do ano de 2023</h2>
    """, unsafe_allow_html=True)
    graf.show_month()
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        Os meses de pico são:
        * Janeiro
        * Março
        * Julho""")
    st.markdown("---")
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Conclusão</h2>
    """, unsafe_allow_html=True)
    st.markdown("""Além disso, busque aumentar as propagandas do streaming nos meses de pico.""")
    
elif atual == 'Análise de Distribuição':
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Análise de Distribuição</h2>
    """, unsafe_allow_html=True)
    
    # Introdução
    st.markdown("""
        <h4 style='font-size: 25px; text-align: justify;'>
            Com a análise temos os seguintes gráficos sobre a Análise de Distribuição:
        </h4>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">
            Histograma de reproduções por faixa etária
        </h2>
    """, unsafe_allow_html=True)
    graf.show_histidades()  # Chama a função para exibir o histograma
    
    # Observações sobre as faixas etárias que mais reproduzem
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        Faixas etárias que mais reproduzem músicas:
        1) 16-24 anos
        2) 41-48 anos
        3) 57-64 anos
    """)

    st.markdown("---")

    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">
            Histograma de duração em segundos das músicas e suas reproduções
        </h2>
    """, unsafe_allow_html=True)

    graf.show_musicduration()

    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    Músicas de 200 à 250 segundos são mais reproduzidas do que as outras
    """)
    st.markdown("---")
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Conclusões</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        Foque mais em propagandas para as faixas etárias que mais consomem música no streaming, 
        e também priorize a progapanda de músicas na média de duração entre 200 à 250 segundos.
    """)

elif atual == 'Análise de Relacionamento':
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Análise de Relacionamento</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h4 style='font-size: 25px; text-align: justify;'>
            Com a análise temos os seguintes gráficos sobre a Análise de Relacionamento:
        </h4>
    """, unsafe_allow_html=True)

    # Gráfico de Comparação entre gêneros escutados e idades dos usuários
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">
            Comparação entre gêneros escutados e idades dos usuários
        </h2>
    """, unsafe_allow_html=True)
    graf.show_comp1()  # Chama a função para exibir o gráfico de comparação entre gêneros e idades
    
    # Observações sobre gêneros e faixas etárias
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        Gêneros preferidos pelas faixas etárias:
        * 16-24: Pop
        * 25-32: Rock
        * 33-40: Rock
        * 41-48: MPB
        * 49-56: Jazz
        * 57-64: MPB
    """)
    st.markdown("---")

    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">
            Comparação entre idades dos usuários e review nas músicas
        </h2>
    """, unsafe_allow_html=True)
    graf.show_comp2()
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
    Temos que as faixas etárias que menos curte as músicas recomendadas é:
    * 16-24 anos
    * 25-32 anos
    * 33-40 anos
    """)
    st.markdown("---")
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Conclusões</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
    Uma possível solução seria recomendar mais os gêneros mais curtidos para pessoas das
    faixas etárias. Além disso também melhorar as recomendações das músicas para as pessoas que
    estão dando reviews negativas sobre as músicas que são recomendadas.
    """)
    

elif atual == 'Análise Categórica':
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Análise Categórica</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h4 style='font-size: 25px; text-align: justify;'>
            Com a análise temos os seguintes gráficos sobre a Análise Categórica:
        </h4>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Gêneros mais escutados</h2>
    """, unsafe_allow_html=True)

    graf.show_genres()

    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    Podemos ver que os gêneros Pop, MPB e Rock são os mais escutados no geral, 
    com porcentagens de 22.1%, 20.9% e 18.7% respectivamente
    """)
    st.markdown("---")

    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Subgêneros mais escutados</h2>
    """, unsafe_allow_html=True)
    graf.show_subgenres()
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
    Podemos ver que o Kpop, Forró e Alternative são os subgêneros mais escutados no geral,
    com porcentagens de 8.2%, 7.1% e 6.9% respectivamente.
    """)
    st.markdown("---")
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Reviews das músicas</h2>
    """, unsafe_allow_html=True)
    graf.show_liked()
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
    Podemos ver que temos uma baixa quantidade de curtidas em relação a não curtidas,
    de aproximadamente 1 a cada 5 reviews são curtidas, algo preocupante.
    """)
    st.markdown("---")
    
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Plataformas mais utilizadas</h2>
    """, unsafe_allow_html=True)
    graf.show_platf()
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Observações</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
    Podemos ver que as plataformas mobile e web são as que mais tem reproduções.
    """)

    st.markdown("---")
    st.markdown("""
        <h2 style="font-size: 40px; text-align: left;">Conclusões</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
    Podemos ver que temos um grande problema com a quantidade de curtidas, então
    uma forma de resolução seria melhorando as recomendações para os usuários.
    """)
    

# Se o usuário escolheu a opção 'Solução'
elif atual == 'Solução':
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

elif atual == 'Informações sobre o grupo':
    integrantes = [
    {"nome": "Gustavo Felipe", "imagem": Gustavo, "funcoes": ["Relatório", "Roteiro"]},
    {"nome": "João Marcus", "imagem": Joao, "funcoes": ["Repositório", "Dashboard e estilização", "Análise Temporal, de Distribuição e Categórica", "Vídeo"]},
    {"nome": "Lorena Oliveira", "imagem": Lorena, "funcoes": ["Pesquisa", "Relatório", "Roteiro", "Vídeo"]},
    {"nome": "Rodrigo Levino", "imagem": Rodrigo, "funcoes": ["Roteiro", "Análise Temporal", "Vídeo"]},
    {"nome": "Ruan Gois", "imagem": Ruan, "funcoes": ["Análise de Relação", "Roteiro"]}
]

    # Título principal
    st.markdown(""" 
        <h2 style="font-size: 40px; text-align: center;">
            Informações do grupo
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(""" 
        <h2 style="font-size: 40px; text-align: center;">
            Integrantes do 1-Bit
        </h2>
        """, unsafe_allow_html=True)

    # Exibir todos os integrantes
    for integrante in integrantes:
        # Exibir a imagem
        st.markdown(f"""
        <div style="text-align: left; display: flex; align-items: center; margin-bottom: 20px;">
            <img src="data:image/png;base64,{integrante['imagem']}"
                style="width: 16%; max-width: 150px; border-radius: 10px; box-shadow: 5px 5px 15px rgba(0,0,0,0.3);"
                alt="Foto de {integrante['nome']}">
            <div style="margin-left: 15px;">
                <h4 style="font-size: 25px; text-align: justify;">
                    {integrante['nome']}
                </h4>
                <ul style="font-size: 16px; list-style-type: disc; padding-left: 20px;">
                    {''.join([f"<li>{funcao}</li>" for funcao in integrante["funcoes"]])}
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
