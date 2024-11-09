import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import time
from matplotlib.patches import ConnectionPatch

df = pd.read_csv(r'C:\Users\reis_\Downloads\music_streaming.csv')
df['date'], df['time'] = pd.to_datetime(df['date'], format='%Y-%m-%d'), pd.to_datetime(df['time'], format='%H:%M:%S')
df['month'], df['hour'] = df['date'].dt.month, df['time'].dt.hour

def show_picos_idade():
    # Criando a figura e os eixos
    fig, ax = plt.subplots(figsize=(12, 6))
    # Gera o histograma no eixo 'ax'
    ax.hist(df['hour'], bins=24, alpha=0.7, color='orange', edgecolor='darkred')
    # Customizações do gráfico
    ax.set_xlabel('Hora do Dia', fontsize=12)
    ax.set_ylabel('Frequência de Reproduções', fontsize=12)
    ax.set_xticks(range(0, 24))
    ax.set_facecolor('#f0f0f0')
    mean_freq = np.mean(np.histogram(df['hour'], bins=24)[0])
    ax.axhline(mean_freq, color='blue', linestyle='dashed', linewidth=2, label=f'Média da Frequência: {mean_freq:.1f}')
    ax.legend(fontsize=12)
    ax.grid(axis='y', alpha=0.75)
    # Exibe o gráfico
    st.pyplot(fig)
    st.write("""
    
    """)

def show_genres():
    # Criando a figura e os eixos
    fig, ax = plt.subplots(figsize=(8, 8))  # Tamanho da figura
    # Definindo as cores para o gráfico de pizza
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0', '#ffcc00']
    # Gera o gráfico de pizza
    ax.pie(df['genre'].value_counts(), labels=df['genre'].unique(),
        autopct='%1.1f%%', startangle=90, colors=colors,
        shadow=True, explode=[0.1 if genre == 'Rock' else 0 for genre in df['genre'].value_counts().index])
    # Customizações do gráfico
    ax.set_title('Distribuição de Gêneros', fontsize=16, fontweight='bold')
    ax.axis('equal')
    ax.set_facecolor('#f0f0f0') 
    plt.setp(ax.texts, size=14)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def show_subgenres():
    # Criando a figura e os eixos com o tamanho especificado
    fig, ax = plt.subplots(figsize=(20, 18))
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0', '#ffcc00'] # Cria a lista colors para ser adicionadas no gráfico
    # Gera o gráfico de pizza
    ax.pie(df['subgenre'].value_counts(), 
        labels=df['subgenre'].unique(),
        autopct='%1.1f%%', 
        startangle=90, 
        textprops={'fontsize': 30},
        shadow=True, 
        explode=[0.1 if genre == 'Samba' else 0 for genre in df['subgenre'].value_counts().index],
        colors=colors)
    # Customizações
    ax.set_title('Distribuição de subgêneros', fontsize=30, fontweight='bold', pad=30)
    ax.axis('equal')
    ax.set_facecolor('#f0f0f0') 
    plt.setp(ax.texts, size=14) 
    plt.tight_layout()
    ax.legend(fontsize=13)
    # Exibir o gráfico no Streamlit
    st.pyplot(fig)

def show_liked():
    # Criando a figura e os eixos com o tamanho especificado
    fig, ax = plt.subplots(figsize=(8, 8)) 
    # Definindo colors e explode
    colors = ['red', 'lightgreen']
    explode = [0.1 if gostou == True else 0 for gostou in df['liked'].unique()]
    # Gera o gráfico
    ax.pie(df['liked'].value_counts(), 
        labels=['Não gostou', 'Gostou'],
        autopct='%1.1f%%', 
        startangle=90, 
        shadow=True,
        explode=explode,
        colors=colors)
    # Customizações
    ax.set_title('Curtiu a música recomendada?', fontsize=16, fontweight='bold')
    ax.axis('equal')
    ax.set_facecolor('#f0f0f0')
    plt.setp(ax.texts, size=14)
    plt.tight_layout()
    # Exibe o gráfico
    st.pyplot(fig)

def show_streamqual():
    # Criando a figura e os eixos com o tamanho especificado
    fig, ax = plt.subplots(figsize=(8, 8))
    # Gera o gráfico
    ax.bar(df['stream_quality'].value_counts().index, 
        df['stream_quality'].value_counts(), color='lightblue')
    # Customizações
    ax.set_xlabel('Qualidade', fontsize=12)
    ax.set_ylabel('Frequência', fontsize=12)
    ax.set_xticks(range(0, 4))
    plt.tight_layout()
    ax.grid(False)
    # Exibe o gráfico
    st.pyplot(fig)

def show_subtypes():
    # Criando a figura e os eixos com o tamanho especificado
    fig, ax = plt.subplots(figsize=(8, 8))
    # Gera o gráfico
    ax.barh(df['subscription_type'].value_counts().index, df['subscription_type'].value_counts(),
            color='lightgreen')
    # Customizações
    ax.set_xlabel("Frequência")
    ax.set_ylabel("Tipo de Assinatura")
    ax.grid(False)
    plt.tight_layout()
    # Exibe o gráfico
    st.pyplot(fig)

def show_platf():
    df2 = df.drop_duplicates(subset='user_id')
    st.subheader('Gráfico de Pizza sobre plataforma das reproduções')
    # Criando a figura e os eixos com o tamanho especificado
    fig, ax = plt.subplots(figsize=(12, 8))
    # Gera o gráfico
    ax.pie(df2['platform'].value_counts(), 
            labels=df2['platform'].unique(), 
            autopct='%1.1f%%', startangle=90,
            shadow=True)
    # Customizações
    ax.axis('equal')
    plt.setp(plt.gca().texts, size=14)
    plt.tight_layout()
    ax.legend(fontsize=16)
    # Exibe o gráfico
    st.pyplot(fig)

def show_month():
    
    # Criando a figura e os eixos com o tamanho especificado
    fig, ax = plt.subplots(figsize=(12 * 1.5, 6 * 1.5))
    
    # Contando a frequência de reproduções por mês
    month_counts = df['month'].value_counts().sort_index()
    
    # Gerando o gráfico de linha
    ax.plot(month_counts.index, month_counts.values, marker='o', color='royalblue', linewidth=2, markersize=8, label='Frequência de Reproduções')
    
    # Customizações do gráfico
    ax.set_xlabel("Mês", fontsize=14)
    ax.set_ylabel("Frequência", fontsize=14)
    ax.set_xticks(range(1, 13))  # Para garantir que os meses fiquem de 1 a 12
    ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], fontsize=12)
    ax.set_title("Distribuição de Reproduções ao Longo dos Meses", fontsize=16, fontweight='bold')

    # Adicionando a linha de média
    mean_freq = np.mean(month_counts)
    ax.axhline(mean_freq, color='red', linestyle='--', linewidth=3, label=f'Média: {mean_freq:.1f}')
    
    # Adicionando a legenda
    ax.legend(fontsize=12)
    
    # Removendo o grid para um visual mais limpo
    ax.grid(False)
    
    # Estilo de fundo mais suave
    ax.set_facecolor('whitesmoke')
    
    # Ajustando o layout do gráfico
    fig.tight_layout()
    
    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

def show_comp1():
    # Criação da pivot table
    pivot = df.pivot_table(index='user_age', columns='genre', aggfunc='size', fill_value=0)
    pivot_reset = pivot.reset_index()

    # Verificação para garantir que a coluna 'user_age' seja tratada corretamente
    if 'user_age' not in pivot_reset.columns:
        pivot_reset['user_age'] = df['user_age']

    # Definindo intervalos de faixas etárias
    intervalos = pd.cut(pivot_reset['user_age'], bins=[15, 24, 32, 40, 48, 56, 64], labels=['16-24', '25-32', '33-40', '41-48', '49-56', '57-64'])
    pivot_reset['Faixa_Etaria'] = intervalos

    # Agrupamento por faixa etária e somando os gêneros
    resultado = pivot_reset.groupby('Faixa_Etaria')[['Electronic', 'Hip Hop', 'Jazz', 'MPB', 'Pop', 'Rock']].sum().reset_index()

    # Recorte das linhas, se necessário
    recorte = resultado.iloc[0:6, 1:7]  # Considerando as faixas etárias corretamente

    # Criando a figura e os eixos
    fig, ax = plt.subplots(figsize=(10, 8))  # Tamanho da figura pode ser ajustado conforme necessário

    # Criando o heatmap com a variável 'ax'
    grafico = sns.heatmap(
        recorte, 
        vmin=0, 
        vmax=recorte.max().max(),  # Definir vmax dinamicamente baseado no máximo valor do recorte
        linewidths=1, 
        cmap='viridis',  # A cor 'viridis' é especificada aqui
        annot=True, 
        fmt='.0f', 
        ax=ax,
        cbar_kws={'label': 'Frequência de Reproduções'}  # Adicionando a legenda para a barra de cores
    )

    # Ajustes do gráfico
    plt.xticks(rotation=40)
    grafico.set_yticklabels(['16-24', '25-32', '33-40', '41-48', '49-56', '57-64'], rotation=0)
    grafico.set(xlabel="Gêneros", ylabel="Faixa Etária")
    plt.title("Perfil dos usuários: gêneros por idade")

    # Exibindo o gráfico corretamente com Streamlit
    st.pyplot(fig)  # Exibindo a figura com Streamlit, sem a necessidade de plt.show()

def show_comp2():
    liked_count = df['liked'].value_counts()  # Conta o número de True (curtidas) e False (não curtidas)
    # Gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)

    # Gráfico de pizza para a distribuição de curtidas
    liked_ratios = [liked_count[True], liked_count[False]]  # Número de curtidas (True) e não curtidas (False)
    labels = ['Gostou', 'Não Gostou']
    explode = [0, 0.1]  # Destacar a fatia de "Não Gostou" um pouco
    angle = -80 * liked_ratios[0]  # Define o ângulo inicial para um melhor layout do gráfico

    # Plotando o gráfico de pizza
    wedges, *_ = ax1.pie(liked_ratios, autopct='%1.1f%%', startangle=angle,
                        labels=labels, explode=explode)

    # Gráfico de barra
    age_ratios = [.2105, .2105, .1842, .1842, .1315, .0789]
    age_labels = ['16-24', '25-32', '33-40', '41-48', '49-56', '57-64']
    bottom = 1
    width = .2
    for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                    alpha=0.1 + 0.18 * j)
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')
    ax2.set_title('Idade dos que usam offline')
    ax2.legend()
    ax2.axis('off')
    ax2.set_xlim(- 2.5 * width, 2.5 * width)
    # Desenhando as linhas entre os gráficos
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(age_ratios)
    # Linha de cima
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                        xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax2.add_artist(con)
    # Linha de baixo
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                        xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(4)
    st.pyplot(fig)

def show_histidades():
    intervalos = pd.cut(df['user_age'], bins=[15, 24, 32, 40, 48, 56, 64], labels=['16-24', '25-32', '33-40', '41-48', '49-56', '57-64'])
    df['Faixa_Etaria'] = intervalos

    # Contagem de usuários por faixa etária
    faixa_etaria_count = df['Faixa_Etaria'].value_counts().sort_index()

    # Criando o gráfico
    fig, ax = plt.subplots(figsize=(12, 8))

    # Gerando o histograma (na verdade, aqui estamos criando um gráfico de barras)
    ax.bar(faixa_etaria_count.index, faixa_etaria_count.values, color='skyblue', edgecolor='black')

    # Definindo títulos e rótulos
    ax.set_title('Distribuição de Usuários por Faixa Etária', fontsize=16)
    ax.set_xlabel('Faixa Etária', fontsize=12)
    ax.set_ylabel('Número de Usuários', fontsize=12)
    ax.grid(False)
    ax.axhline(y=faixa_etaria_count.mean(), color='red', linestyle='--', label=f'Média: {faixa_etaria_count.mean():.2f}')
    plt.tight_layout()
    plt.legend(fontsize=12)
    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

def show_musicduration():
    # Criando a figura e os eixos
    fig, ax = plt.subplots(figsize=(10, 6))

    # Criando o histograma para a coluna 'duration_seconds' do dataframe
    ax.hist(df['duration_seconds'], bins=30, color='orange', edgecolor='black')

    # Adicionando título e rótulos aos eixos
    ax.set_title('Distribuição da Duração das Músicas em Segundos', fontsize=16)
    ax.set_xlabel('Duração (Segundos)', fontsize=14)
    ax.set_ylabel('Frequência', fontsize=14)

    # Cálculo da média da frequência (média da quantidade de músicas em cada intervalo de tempo do histograma)
    hist_values, bin_edges = np.histogram(df['duration_seconds'], bins=30)
    mean_freq = np.mean(hist_values)

    # Adicionando uma linha horizontal para a média da frequência
    plt.axhline(mean_freq, color='darkblue', linestyle='dashed', linewidth=2, label=f'Média da Frequência: {mean_freq:.1f}')

    # Adicionando a legenda
    ax.legend()

    # Ajustando layout
    plt.tight_layout()
    ax.grid(False)

    # Exibindo o gráfico
    st.pyplot(fig)