# Streaming de Música - Dashboard de Análise

Este projeto apresenta um **dashboard interativo** criado com o Streamlit para análise de dados de um serviço de streaming de música. Utilizando o **Python**, bibliotecas como `pandas`, `matplotlib`, `seaborn` e funções customizadas, a aplicação permite realizar diversas análises sobre os dados de streaming e gerar insights sobre os comportamentos dos usuários.

## Funcionalidades

O dashboard está dividido em várias seções, cada uma com diferentes tipos de análise. O usuário pode selecionar as opções no menu lateral para explorar as seguintes análises:

1. **Introdução**
2. **Análise Temporal**
3. **Análise de Distribuição**
4. **Análise de Relacionamento**
5. **Análise Categórica**
6. **Solução**
7. **Informações sobre o Grupo**

### 1. Introdução

Apresenta uma introdução ao conceito do projeto, explicando a proposta de um sistema de recomendação de músicas para plataformas de streaming.

### 2. Análise Temporal

Explora a evolução temporal das reproduções de músicas ao longo do tempo. Inclui gráficos de horários de pico e frequência de reproduções por mês.

- **Horários de pico de visualizações**
- **Frequência de reproduções por mês (2023)**

### 3. Análise de Distribuição

Examina como a distribuição dos dados está distribuída entre diferentes faixas etárias e durações das músicas. Inclui os seguintes gráficos:

- **Histograma de reproduções por faixa etária**
- **Histograma de duração das músicas e suas reproduções**

### 4. Análise de Relacionamento

Investiga as relações entre diferentes variáveis, como gêneros musicais preferidos por diferentes faixas etárias, comparando preferências de música entre os usuários e outros fatores.

- **Comparação entre gêneros escutados e idades dos usuários**
- **Comparação entre idades dos usuários e avaliação das músicas**

### 5. Análise Categórica

Examina as categorias mais relevantes, como gêneros e subgêneros musicais, e a análise de curtidas ou não curtidas nas músicas.

- **Gêneros mais escutados**
- **Subgêneros mais escutados**
- **Plataformas mais utilizadas**

### 6. Solução

Apresenta uma proposta de solução para melhorar as recomendações de músicas, baseando-se em como as plataformas como **Spotify** e **YouTube** utilizam algoritmos personalizados para fornecer recomendações.

### 7. Informações sobre o Grupo

Exibe informações sobre os membros do grupo responsável pelo desenvolvimento do projeto, suas funções e contribuições.

## Tecnologias Utilizadas

- **Streamlit**: Para criar a interface interativa do dashboard.
- **Pandas**: Para manipulação e análise de dados.
- **Matplotlib** e **Seaborn**: Para visualização dos dados.
- **Base64**: Para exibição de imagens no Streamlit sem precisar de arquivos externos.
- **Python 3.x**

## Como Rodar

1. Instale as dependências:

```bash
pip install streamlit pandas matplotlib seaborn
```
2. Execute o aplicativo Streamlit:
```bash
streamlit run dashboard.py
```
3. O aplicativo será iniciado no seu navegador, onde você poderá interagir com o dashboard e explorar os dados.

## Estrutura do Código

### Funções

`img_to_base64(caminho_imagem: str) -> str`

Função que converte uma imagem para formato Base64, permitindo exibi-la diretamente no Streamlit.

### Pré-processamento de Dados

* O arquivo CSV `music_streaming.csv` é carregado e processado, com as colunas `date` e `time` sendo convertidas para o formato datetime.

* A extração do mês e da hora a partir da data e hora é realizada para análise temporal.

### Barra Lateral do Streamlit

A barra lateral permite que o usuário escolha entre diferentes gráficos e seções do dashboard. Cada opção carrega um conjunto de análises específicas, incluindo visualizações gráficas e interpretações dos dados.

---

## Licença

Este projeto está sob a licença *MIT*. Veja o arquivo LICENSE para mais informações.

---

## Contribuidores

* Gustavo Felipe: Relatório, Roteiro.
* João Marcus: Repositório, Dashboard e estilização, Análise Temporal, de Distribuição e Categórica, Vídeo.
* Lorena Oliveira: Pesquisa, Relatório, Roteiro, Vídeo.
* Rodrigo Levino: Roteiro, Análise Temporal, Vídeo.
* Ruan Gois: Análise de Relação, Roteiro.