#Libraries
import pandas as pd
import inflection
import plotly.graph_objects as go
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static

#Funções
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America"
    }

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred"
    }

def country_name(country_id):
  return COUNTRIES[country_id]

def color_name(color_code):
  return COLORS[color_code]

def rename_columns(dataframe):
  df = dataframe.copy()
  title = lambda x: inflection.titleize(x)
  sneakecase = lambda x: inflection.underscore(x)
  spaces = lambda x: x.replace(" ", "")
  cols_old = list(df.columns)
  cols_old = list(map(title, cols_old))
  cols_old = list(map(spaces, cols_old))
  cols_new = list(map(sneakecase, cols_old))
  df.columns = cols_new

  return df

def create_price_type(price_range):
  if price_range == 1:
    return "cheap"
  elif price_range == 2:
    return "normal"
  elif price_range == 3:
    return "expensive"
  else:
    return "gourmet"
  
def clean_code(df):
  #Limpeza dos Dados
  #1 - Remover linhas duplicadas
  df1 = df.drop_duplicates(ignore_index=True)

  #2 - Organizar e renomear os nomes das colunas
  df1 = rename_columns(df1)

  #3 - Alterar o código do país para seu respectivo nome
  df1['country_code'] = df1['country_code'].map(country_name)
  df1.rename(columns={'country_code': 'country'}, inplace=True)

  #4 - Alterar o código das cores para o nome da cor
  df1['rating_color'] = df1['rating_color'].map(color_name)

  #5 - Criação da categoria do tipo de comida de acordo com o range
  df1['price_range'] = df1['price_range'].map(create_price_type)

  #6 - Categorizando todos os restaurantes para somente um tipo de culinária
  df1['cuisines'] = (df1.loc[:, 'cuisines']
                        .astype(str)
                        .apply(lambda x: x.split(',') [0]))

  #7 - Removendo as linhas 'nan' da coluna 'cuisines'
  linhas_selecionadas = (df1['cuisines'] != 'nan')
  df1 = df1.loc[linhas_selecionadas, :].copy()

  return df1

def count_countries (df1, count_col):
  if count_col == 'restaurant_id':
    df_aux = (df1.loc[:,['country','restaurant_id']]
                .groupby('country')
                .count()
                .sort_values('restaurant_id',ascending=False)
                .reset_index())

    fig = px.bar(df_aux, x='country', y='restaurant_id', text_auto='restaurant_id', labels={'country':'Países', 'restaurant_id':'Total de Restaurantes'}, 
                title='Quantidade de Restaurantes registrados por País')
    fig.update_layout(title_x = 0.5)
    fig = st.plotly_chart(fig, use_container_width=True)
    return fig

  else:
    df_aux = (df1.loc[:,['country','city']]
                .groupby('country')
                .nunique()
                .sort_values('city',ascending=False)
                .reset_index())

    fig = px.bar(df_aux, x='country', y='city', text_auto='city', labels={'country':'Países', 'city':'Total de Cidades'}, title='Quantidade de Cidades registradas por País')
    fig.update_layout(title_x = 0.5)
    fig = st.plotly_chart(fig, use_container_width=True)
    return fig

def mean_country(df1, mean_col):
  if mean_col == 'votes':
    df_aux = (round(df1.loc[:, ['country', 'votes']]
                     .groupby('country')
                     .mean()
                     .sort_values('votes', ascending=False),2)
                     .reset_index())

    fig = px.bar(df_aux, x='country', y='votes', text_auto='votes', 
                labels={'country':'Países', 'votes':'Média de Avaliações'}, 
                title='Média de Avaliações por País')
    fig.update_layout(title_x = 0.5)
    fig = st.plotly_chart(fig, use_container_width=True)
    return fig
  else:
    df_aux = (round(df1.loc[:, ['country', 'average_cost_for_two']]
                     .groupby('country')
                     .mean()
                     .sort_values('average_cost_for_two', ascending=False)
                     .reset_index(),2))

    fig = px.bar(df_aux, x='country', y='average_cost_for_two', text_auto='average_cost_for_two', 
                labels={'country':'Países', 'average_cost_for_two':'Preço de um prato para duas pessoas'}, 
                title='Média de preço de um prato para dois')
    fig.update_layout(title_x = 0.5)
    fig = st.plotly_chart(fig, use_container_width=True)
    return fig

#--------------Início da Estrutura lógica do código--------------------------------------
#-------------------
#Import dataset
#-------------------
df = pd.read_csv('dataset/zomato.csv')

#Limpeza dos Dados
df1 = clean_code(df)

st.set_page_config('Visão Países', layout='wide')
st.header('🌎Visão Países')
st.markdown('___')
st.subheader('Countries Metrics')

# =======================================
# BARRA LATERAL
# =======================================
st.sidebar.image('logo.png',width=150)
st.sidebar.markdown('# Fome Zero Restaurant')
st.sidebar.markdown('### Taste the best cuisines of the world.')
st.sidebar.markdown('___')
st.sidebar.markdown('## Filtros:')

lista_paises = ["India",
"Australia",
"Brazil",
"Canada",
"Indonesia",
"New Zeland",
"Philippines",
"Qatar",
"Singapure",
"South Africa",
"Sri Lanka",
"Turkey",
"United Arab Emirates",
"England",
"United States of America"]

country_options = st.sidebar.multiselect(options=lista_paises, label='Selecione os países que deseja analisar:', 
                                         default=["Australia", "Brazil", "England", "India", "South Africa", "United States of America"])

st.sidebar.markdown('___')

st.sidebar.markdown('## Dados tratados:')
st.sidebar.download_button(label='Download', data='dataset/zomato.csv')
st.sidebar.markdown('___')
st.sidebar.markdown('###### Powered by Marcos Paulo | mpcruz®')

#Filtro de trânsito
linhas_selecao = df1['country'].isin(country_options)
df1 = df1.loc[linhas_selecao, :]

# =======================================
# LAYOUT PRINCIPAL NO STREAMLIT
# =======================================
 
#Quantidade de Restaurantes registrados por País
count_countries(df1, 'restaurant_id')

#Quantidade de Cidades registrados por País
count_countries(df1, 'city')

col1, col2 = st.columns(2, gap='large')
with col1:
  #Média de Avaliações por País
  mean_country(df1, 'votes')
  

with col2:
  #Média de Preço de um prato para dois por País
  mean_country(df1, 'average_cost_for_two')
  
