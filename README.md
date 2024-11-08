# Dashboard de Análise de Streaming de Música

Este projeto tem como objetivo a análise de dados de streaming de música utilizando o **Streamlit**, **Matplotlib** e **Seaborn**. Através deste dashboard interativo, é possível explorar diversos aspectos do comportamento dos usuários em relação ao consumo de música.

## Descrição

O dashboard utiliza um dataset de streaming de música para gerar gráficos e insights sobre os seguintes aspectos:

- **Horários de pico de reprodução**
- **Distribuição de gêneros e subgêneros**
- **Reações dos usuários** (curtidas ou não)
- **Qualidade do stream**
- **Tipos de assinaturas**
- **Plataformas utilizadas**
- **Análise temporal** (mês de reprodução)
- **Comparação entre faixas etárias e gêneros musicais**
- **Análise do uso do modo offline vs online por faixa etária**

## Pré-requisitos

Para rodar este projeto, é necessário ter o Python 3.x e os seguintes pacotes instalados:

- **streamlit**
- **pandas**
- **matplotlib**
- **seaborn**
- **numpy**
- **base64**

Você pode instalar as dependências usando o `pip`:
```
pip install streamlit pandas matplotlib seaborn numpy
```
## Como rodar

1. Clone o repositório para sua máquina local.
2. Certifique-se de que o dataset `music_streaming.csv` esteja disponível na mesma pasta que o script.
3. No terminal, navegue até o diretório onde o script está localizado e execute o seguinte comando para iniciar o dashboard:
```
python -m streamlit run dashboard.py
```

O Streamlit abrirá o dashboard em seu navegador.

## Funcionalidades do Dashboard

### 1. **Visão Geral de Gêneros**

- **Objetivo:** Exibir a distribuição de gêneros musicais presentes no dataset.
- **Componentes:**
  - **Gráfico de barras** mostrando a quantidade de streamings por gênero musical.

### 2. **Análise de Horário de Pico**

- **Objetivo:** Identificar os horários de pico de streaming.
- **Componentes:**
  - **Gráfico de linha** mostrando o número de streamings ao longo das horas do dia.

### 3. **Reações dos Usuários**

- **Objetivo:** Analisar as reações dos usuários, como curtidas ou não.
- **Componentes:**
  - **Gráfico de barras** mostrando a quantidade de reações positivas e negativas para cada gênero.

### 4. **Comparação entre Faixa Etária e Gêneros Musicais**

- **Objetivo:** Analisar como diferentes faixas etárias se comportam em relação aos gêneros musicais.
- **Componentes:**
  - **Gráfico de barras empilhadas** mostrando a distribuição de faixas etárias para cada gênero musical.

### 5. **Qualidade de Streaming**

- **Objetivo:** Mostrar como os usuários se comportam em relação à qualidade do streaming.
- **Componentes:**
  - **Gráfico de barras** mostrando a quantidade de streamings por qualidade.

### 6. **Tipos de Assinatura**

- **Objetivo:** Exibir a distribuição dos tipos de assinaturas dos usuários.
- **Componentes:**
  - **Gráfico de barras** mostrando a quantidade de streamings por tipo de assinatura (premium, gratuito, etc.).

### 7. **Plataformas Utilizadas**

- **Objetivo:** Mostrar a popularidade das plataformas usadas para o streaming de músicas.
- **Componentes:**
  - **Gráfico de barras** mostrando a quantidade de streamings por plataforma.

### 8. **Análise Temporal**

- **Objetivo:** Mostrar a distribuição de streamings ao longo dos meses.
- **Componentes:**
  - **Gráfico de linha** mostrando a quantidade de streamings por mês.

### 9. **Modo Offline vs Online por Faixa Etária**

- **Objetivo:** Comparar o uso do modo offline vs online em diferentes faixas etárias.
- **Componentes:**
  - **Gráfico de barras empilhadas** mostrando a distribuição entre os modos offline e online por faixa etária.

## Considerações Finais

Este projeto visa proporcionar uma visão mais clara e detalhada sobre os hábitos de consumo de música dos usuários, permitindo identificar padrões e tendências em tempo real. O uso de ferramentas como **Streamlit**, **Seaborn** e **Matplotlib** torna a análise interativa e visualmente atraente.