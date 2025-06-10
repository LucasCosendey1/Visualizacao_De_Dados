import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.title('Análise da Desigualdade no Acesso ao Ensino Superior Brasileiro')

st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 2, 1])
col2.write("### RESUMO")

col1, col2, col3 = st.columns([1, 5, 1])
col2.write("""            
Este trabalho tem como objetivo analisar dados educacionais fornecidos pelo IBGE, com foco
nas diferenças de acesso e permanência no ensino superior entre homens e mulheres, assim
como nas disparidades de renda entre estudantes de instituições públicas e privadas. Através
de gráficos e tabelas, busca-se compreender a distribuição dos alunos de acordo com o perfil
socioeconômico, além de relacionar esses dados com informações sobre os motivos que
levam os jovens a abandonar o ensino médio. Um dos achados mais relevantes mostra que há
maior presença de mulheres nas universidades, enquanto entre os homens o abandono escolar
é mais comum por motivos relacionados à necessidade de trabalhar. A análise foi realizada
com o uso de Python e ferramentas de visualização de dados, permitindo interpretações claras
e fundamentadas sobre o cenário atual da educação no Brasil.

""")


st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)



tabela = {
    'Distribuição(%)': [
        'Total Pública', 'Total Privada', 'fundamental Pública', 'fundamental Privada',
        'médio Pública', 'médio Privada', 'superior Pública', 'superior Privada'
    ],
    'Total': [8096.98, 2390.84, 22412.48, 4754.46, 7587.87, 1125.28, 2412.54, 6381.90],
    'Sexo(Homem)': [50.15, 51.30, 52.28, 50.96, 49.60, 47.28, 48.50, 41.80],
    'Sexo(Mulher)': [49.85, 48.70, 47.72, 49.04, 50.40, 52.72, 51.40, 58.20],
    'Classe E': [36.25, 9.19, 39.54, 8.07, 31.56, 6.78, 10.33, 5.68],
    'Classe D': [28.19, 13.74, 28.52, 13.73, 26.97, 9.27, 14.76, 11.20],
    'Classe C': [17.68, 16.50, 17.54, 15.26, 20.30, 13.82, 18.39, 17.65],
    'Classe B': [12.96, 20.74, 10.54, 24.60, 15.08, 23.12, 24.72, 29.13],
    'Classe A': [4.92, 39.84, 3.87, 38.35, 6.08, 47.01, 31.79, 36.33]
}

df = pd.DataFrame(tabela)

st.write("#### Tabela empregada na extração de insights apresentados no artigo.")
st.dataframe(df)



st.markdown("<div style='margin-top: 150px;'></div>", unsafe_allow_html=True)


st.header("INTRODUÇÃO")
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

st.write("""            
A educação é um dos pilares fundamentais para o desenvolvimento individual e
coletivo de uma sociedade. No Brasil, o acesso ao ensino superior tem crescido ao longo dos
anos, mas ainda revela desigualdades significativas relacionadas ao tipo de instituição
frequentada (pública ou privada), à renda familiar e ao gênero dos estudantes. Ao analisar
esses fatores, é possível identificar padrões que revelam não apenas as disparidades no acesso
ao ensino, mas também as barreiras estruturais que dificultam a permanência dos estudantes
nas instituições de ensino.
         
Este trabalho tem como objetivo realizar uma análise exploratória dos dados educacionais
disponibilizados pelo IBGE, com foco especial nas desigualdades de acesso entre homens e
mulheres no ensino superior, nas diferenças de renda entre estudantes de instituições públicas
e privadas e nos principais motivos que levam os jovens a abandonarem os estudos antes de
concluir o ensino médio. Entre os dados mais relevantes, destaca-se a maior presença
feminina no ensino superior em comparação aos homens, além do impacto da necessidade de
trabalhar como um dos principais fatores de evasão escolar entre o público masculino.
         
A análise foi realizada por meio de gráficos e tabelas, com uso da linguagem Python e
bibliotecas como Pandas e Matplotlib, possibilitando a visualização clara dos dados e o
desenvolvimento de reflexões a partir dos resultados. Ao final, espera-se compreender melhor
como fatores socioeconômicos e de gênero influenciam a trajetória educacional no Brasil e
como essas desigualdades se manifestam nas estatísticas mais recentes.
""")


st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

st.header('OBJETIVOS')

col1, col2, col3 = st.columns([1, 10, 5])

col2.write("### Objetivo Geral:")
st.write("""O objetivo deste trabalho é analisar a relação entre a renda familiar e o acesso ao
ensino superior no Brasil, com base em dados do IBGE, destacando também os principais
motivos que levam os estudantes a abandonarem o ensino médio. A partir dessa análise,
busca-se compreender como fatores socioeconômicos influenciam a permanência e o ingresso
nas instituições públicas e privadas de ensino superior.
""")

st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 10, 5])

col2.write("### Objetivos Específicos:")
st.write("""● Identificar a distribuição percentual da renda entre os estudantes das universidades
públicas e privadas;

● Comparar a proporção de homens e mulheres no acesso às universidades públicas e
privadas, a fim de identificar possíveis desigualdades de gênero no ensino superior.

● Verificar os principais motivos para abandono escolar no ensino médio, com recorte de
gênero;

""")



st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

st.header('FONTES DE DADOS')
st.write("""Este trabalho tem como base a análise de dados secundários disponibilizados pelo Instituto
Brasileiro de Geografia e Estatística (IBGE), extraídos do relatório “Síntese de Indicadores
Sociais: Uma Análise das Condições de Vida da População Brasileira 2023”. Os dados foram
obtidos através do portal oficial do IBGE, disponível no link:
https://www.ibge.gov.br/estatisticas/sociais/trabalho/9221-sintese-de-indicadores-sociais.html
         
Entre os arquivos disponibilizados na seção de resultados, foi utilizado o arquivo compactado
denominado "Educação (xls)", que contém diversas planilhas em formato Excel. Dentre elas,
foram selecionadas duas planilhas principais para análise:

● Tabela 4.5 (RedeAdm_BR).xls: apresenta a distribuição percentual dos estudantes
brasileiros por tipo de rede de ensino (pública ou privada) e por nível de escolaridade,
cruzando essas variáveis com a classe de renda dos domicílios.

● Período: Anual.

● Ano: 2016 - 2022

● Tabela 4.17 (SemEnsinoMedioMotivNaoFreq_BR).xls: apresenta os principais
motivos declarados pelas pessoas de 14 a 29 anos de idade para não frequentarem ou
terem abandonado o ensino médio, segmentados por sexo.

● Período: Anual.

● Ano: 2022

A análise dos dados foi realizada utilizando a linguagem de programação Python em
ambiente Jupyter Notebook, por meio de bibliotecas como pandas, para manipulação de
dados, e matplotlib, para visualização gráfica. Foram produzidos gráficos do tipo pizza,
barras horizontais e tabelas customizadas com o objetivo de facilitar a interpretação dos
dados.
         
Além disso, foram aplicadas técnicas básicas de limpeza e transformação de dados,
incluindo arredondamento de valores, conversão de formatos e seleção de colunas e linhas
relevantes para os objetivos do estudo. Nenhuma inferência estatística foi realizada, pois o
foco do trabalho está na descrição e interpretação visual dos dados apresentados.
""")


st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

st.header("ANÁLISE E INTERPRETAÇÃO DOS DADOS")
st.write("""Nesta seção, são apresentados e interpretados os dados coletados com o objetivo de
compreender os fatores que contribuem para o abandono escolar no Brasil, com ênfase nas
desigualdades sociais e de gênero. A análise foi conduzida com base em informações
extraídas de planilhas educacionais e representadas por meio de gráficos, permitindo observar
com maior clareza as disparidades entre diferentes grupos sociais ao longo dos anos.
         
Para isso, utilizou-se a análise exploratória de dados, com o apoio de visualizações gráficas,
tabelas comparativas e percentuais de distribuição. O foco esteve em identificar padrões
recorrentes, variações por classe social e sexo, e relações com aspectos socioeconômicos que
influenciam diretamente a permanência ou evasão de estudantes nos níveis fundamentais,
médios e superiores da educação
""")

st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 10, 5])



GraficoDeBarra = {
    'Precisou trabalhar': [
        'Homem', 'Mulher'
    ],
    'Distribuição(%)': [51.73, 23.88]
}

df = pd.DataFrame(GraficoDeBarra)

# Gráfico
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df['Precisou trabalhar'], df['Distribuição(%)'], color=['blue', 'pink'])

# Personalização
ax.set_ylabel('Distribuição (%)')
ax.set_title('Motivo de abandono escolar: Precisou trabalhar')
ax.set_ylim(0, 60)  # Ajuste para melhor visualização dos dados
for i, v in enumerate(df['Distribuição(%)']):
    ax.text(i, v + 1, f'{v}%', ha='center', fontweight='bold')

# Exibir no Streamlit
st.pyplot(fig)



st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

st.write("""Um dos aspectos mais relevantes na análise da evasão escolar no Brasil está
relacionado aos motivos que levam estudantes a interromperem sua trajetória educacional. A
imagem acima ilustra um desses motivos: a necessidade de trabalhar. Os dados revelam uma
disparidade marcante entre os gêneros.
         
Enquanto 51,73% dos homens apontam o trabalho como o principal motivo para o abandono
escolar, apenas 23,88% das mulheres indicam essa razão. Essa diferença significativa
evidencia que o abandono escolar por necessidade de inserção no mercado de trabalho afeta
muito mais os homens do que as mulheres.
         
Essa realidade pode ser interpretada à luz de fatores socioculturais e econômicos.
Historicamente, homens tendem a ser pressionados a contribuir financeiramente com suas
famílias desde cedo, o que pode levá-los a priorizar o trabalho em detrimento da educação
formal. Por outro lado, embora as mulheres também enfrentam desafios econômicos, muitas
vezes acumulam responsabilidades domésticas e de cuidado, o que pode levá-las a abandonar
os estudos por outros motivos, como gravidez ou afazeres familiares — questões que também
merecem atenção em uma análise ampliada da evasão escolar.
         
Este dado reforça a importância de políticas públicas que garantam a permanência dos jovens
na escola, sobretudo os de baixa renda, por meio de programas de assistência financeira,
flexibilização de horários escolares e incentivos ao primeiro emprego vinculado à
continuidade dos estudos.
""")


st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 10, 5])
col2.write("### Participação Feminina no Ensino Superior")
 


# Dados organizados
dados = {
    'Sexo': ['Feminino', 'Masculino', 'Feminino', 'Masculino'],
    'Tipo': ['Público', 'Público', 'Privado', 'Privado'],
    'Distribuição(%)': [51.4, 48.5, 58.2, 41.8]
}

df = pd.DataFrame(dados)

# Preparar posições
labels = ['Público', 'Privado']
x = np.arange(len(labels))  # [0, 1]
largura = 0.35

# Separar valores
feminino = df[df['Sexo'] == 'Feminino']['Distribuição(%)'].values
masculino = df[df['Sexo'] == 'Masculino']['Distribuição(%)'].values

# Criar gráfico
fig, ax = plt.subplots(figsize=(8, 4))

b1 = ax.bar(x - largura/2, masculino, largura, label='Masculino', color='blue')
b2 = ax.bar(x + largura/2, feminino, largura, label='Feminino', color='pink')

# Personalização
ax.set_ylabel('Distribuição (%)')
ax.set_title('Participação de Homens e Mulheres no Ensino Superior')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(0, 70)
ax.legend()

# Adicionar rótulos nas barras
for barras in [b1, b2]:
    for barra in barras:
        altura = barra.get_height()
        ax.annotate(f'{altura:.2f}%',
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

# Exibir no Streamlit
st.pyplot(fig)


st.write("""
A imagem acima revela uma importante característica da educação superior no Brasil: a
predominância feminina entre os estudantes matriculados tanto em instituições públicas
quanto privadas de ensino superior. De acordo com os dados, 51,40% dos alunos das
universidades públicas são mulheres, frente a 48,50% de homens. A diferença se acentua nas
instituições privadas, onde as mulheres representam 58,20%, enquanto os homens somam
apenas 41,80%.
         
Essa desigualdade de gênero no ensino superior pode ser explicada, em parte, pela evasão
escolar masculina pela necessidade de começar a trabalhar antes mesmo da conclusão do
ensino médio. Essa realidade reflete uma pressão sociocultural sobre os homens para
contribuir financeiramente com suas famílias desde cedo, o que compromete sua permanência
na educação formal e, consequentemente, reduz suas chances de ingresso no ensino superior.
         
Embora as mulheres também enfrentam obstáculos, como responsabilidades domésticas e
questões relacionadas à maternidade, elas tendem a permanecer mais tempo na escola e a
buscar maior qualificação acadêmica. Por isso, é fundamental que políticas públicas de
permanência escolar levem em consideração essas diferenças de gênero, criando mecanismos
de apoio especialmente voltados para jovens de baixa renda que enfrentam a necessidade de
trabalhar antes de concluir seus estudos.
""")


st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 10, 5])
col2.write("### Desigualdade de Acesso: O Ensino Superior e a Exclusão das Classes Baixas")

st.write("""
Apesar de as universidades públicas brasileiras terem sido idealizadas para promover
inclusão social e democratizar o acesso ao ensino superior, os dados revelam um cenário
contraditório. Ao analisarmos a distribuição de renda dos estudantes matriculados nessas
instituições, percebemos que o público atendido está longe de refletir a população de baixa
renda, que deveria ser a principal beneficiária das políticas públicas educacionais.
""")




dados = {
    'Classe': ['Classe A', 'Classe B', 'Classe C', 'Classe D', 'Classe E'],
    'Distribuição(%)': [31.79, 24.72, 18.39, 14.76, 10.33]
}
df = pd.DataFrame(dados)


cores_personalizadas = {
    'Classe A': 'blue',
    'Classe B': 'green',
    'Classe C': 'brown',
    'Classe D': 'orange',
    'Classe E': 'red'
}


fig = px.pie(
    df,
    names='Classe',
    values='Distribuição(%)',
    color='Classe',
    color_discrete_map=cores_personalizadas,
    title='Distribuição de Renda - Universidade Pública',
    hole=0  
)

fig.update_traces(textinfo='percent+label', pull=[0.01]*5, hoverinfo='label+percent+value')

# Exibir no Streamlit
st.plotly_chart(fig, use_container_width=True)



st.write("""
Na imagem acima, observa-se que as classes mais altas predominam nas universidades
públicas: a Classe A representa 31,79% dos estudantes, seguida pela Classe B com
24,72%. Enquanto isso, as classes D e E, que correspondem à parcela mais vulnerável da
sociedade, somam juntas apenas 25,09% da população universitária. Isso demonstra que,
mesmo sendo gratuitas, as universidades públicas ainda estão concentradas nas mãos das
elites, em parte porque estudantes dessas classes têm acesso a uma formação básica de maior
qualidade, especialmente em escolas particulares, o que os prepara melhor para exames como
o ENEM e vestibulares concorridos.
         
Em contraste, as universidades privadas, muitas vezes vistas como alternativas para quem
não consegue vaga nas públicas, apresentam uma distribuição de renda semelhante, mas
com ainda menor participação das classes mais baixas.
""")





dados = {
    'Classe': ['Classe A', 'Classe B', 'Classe C', 'Classe D', 'Classe E'],
    'Percentual': [36.3, 29.1, 17.7, 11.2, 5.7]
}
df = pd.DataFrame(dados)


cores_personalizadas = {
    'Classe A': 'blue',
    'Classe B': 'green',
    'Classe C': 'brown',
    'Classe D': 'orange',
    'Classe E': 'red'
}


fig = px.pie(
    df,
    names='Classe',
    values='Percentual',
    color='Classe',
    color_discrete_map=cores_personalizadas,
    title='Distribuição de Renda - Universidade Privada',
    hole=0  
)

fig.update_traces(textinfo='percent+label', pull=[0.01]*5, hoverinfo='label+percent+value')

# Exibir no Streamlit
st.plotly_chart(fig, use_container_width=True)

