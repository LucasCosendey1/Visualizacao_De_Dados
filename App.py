import streamlit as st
import pandas as pd


st.title('Análise da Desigualdade no Acesso ao Ensino Superior Brasileiro')

st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 2, 1])
col2.write("### RESUMO")


col1, col2, col3 = st.columns([1, 2, 1])
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



st.write("""            
### INTRODUÇÃO
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

st.header('swegrerghehgehe')