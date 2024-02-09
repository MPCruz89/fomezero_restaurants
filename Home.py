import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home'
)

# =======================================
# BARRA LATERAL
# =======================================

st.sidebar.image(image='logo.png', width=120)
st.sidebar.markdown('# Fome Zero Restaurant')
st.sidebar.markdown('### Taste the best cuisines of the world.')
st.sidebar.markdown('___')

st.sidebar.markdown('###### Powered by Marcos Paulo | mpcruz®')

# =======================================
# LAYOUT PRINCIPAL NO STREAMLIT
# =======================================

st.header('Fome Zero Dashboards')
st.subheader('Os melhores restaurantes do mundo em um só lugar')
st.markdown('___')

st.markdown('#### Como Utilizar esse Growth Dashboard?')
st.write('###### Este Dashboard foi elaborado para fornecer métricas de acompanhamento e crescimento solicitados pelo CEO da empresa.')

st.markdown('⚙️ VISÃO GERAL')
st.write('###### Uma visão objetiva das métricas gerais da empresa e a possibilidade de encontrar o restaurante mais próximo.')

st.markdown('🌎 VISÃO PAÍSES')
st.write('###### Descreve a quantidade de restaurantes e cidades por país, bem como a média de avaliações e a média de preço de um prato para duas pessoas.')

st.markdown('🏙️ VISÃO CIDADES')
st.write('###### Análise das métricas classificadas por cidades, considerando avaliações dos restaurantes, tipos de culinárias disponíveis e os valores cobrados.')

st.markdown('🛎️ VISÃO RESTAURANTES')
st.write('###### Métricas gerais dos restaurantes, tais como: melhores restaurantes, restaurantes com mais avaliações e aqueles que reservam mesa e realizam entregas.')

st.markdown('🍽️ VISÃO CULINÁRIAS')
st.write('###### Análise das métricas relacionadas aos diversos tipos de culinárias, incluindo os melhores restaurantes por cada tipo de culinária.')

st.markdown('___')
st.markdown('### Contato do Cientista de Dados:')
st.write('##### Time de Data Science no Discord')
st.markdown('###### @mpcruz')



#Resumo Geral:
#A Visao destaca o crescimento da empresa, evidenciando sua expansão para mais países, cidades e restaurantes.
#Análise por País:
#Descreve a análise de dados quantitativos dos restaurantes, incluindo o número de avaliações e o custo médio para duas pessoas em vários países.
#Análise por Cidade:
#Esta análise examina como os restaurantes estão espalhados pelas cidades, considerando suas avaliações e os tipos de comida que servem.
#Análise de Restaurantes:
#Avalia os restaurantes com base em critérios como melhores avaliações e maior número de votos, além de comparar os preços conforme o tipo de culinária e os serviços oferecidos.
#Análise de Cozinhas:
#Examina o preço médio de uma refeição para duas pessoas em diferentes tipos de cozinhas, identificando aquelas com melhores avaliações e a quantidade de restaurantes que oferecem serviços adicionais.

