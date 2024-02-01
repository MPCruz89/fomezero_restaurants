#Libraries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static

#Import csv_file
df = pd.read_csv('dataset/zomato.csv')

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

def top_votes_restaurantes(df1):
  df_aux = (df1.loc[:, ['country','restaurant_name', 'votes']]
              .groupby(['country','restaurant_name'])
              .max().sort_values('votes', ascending=False)
              .reset_index())

  fig = px.bar(df_aux.head(cities_options), x='restaurant_name', y='votes', text_auto='votes',
        labels={'restaurant_name':'Nome do Restaurante', 'votes':'Quantidade de avaliações', 'country': 'País'},
        title=f'Os {cities_options} Restaurantes que possuem mais avaliações', color = 'country')
  graf = st.plotly_chart(fig, use_container_width=True)
  return graf

def online_delivery_restaurants(df1):
  df1_aux = (df1.loc[:, ['has_online_delivery', 'votes']]
              .groupby('has_online_delivery')
              .mean().sort_values('votes')
              .reset_index())

  fig = px.pie(df1_aux, values='votes', names={'0': 'Não entregam', '1': 'Entregam'}, title='Restaurantes que realizam entrega online')
  fig.update_traces(textposition='inside', textinfo='percent+label')
  fig = st.plotly_chart(fig, use_container_width=True)
  return fig

def table_booking_restaurants(df1):
  df_aux = (df1.loc[:, ['has_table_booking', 'average_cost_for_two']]
              .groupby('has_table_booking')
              .mean()
              .sort_values('average_cost_for_two')
              .reset_index())

  fig = px.pie(df_aux, values='average_cost_for_two', names={'0': 'Não aceitam', '1': 'Aceitam Reservas'}, 
              title='Restaurantes que aceitam reservas', 
              labels={'average_cost_for_two':'média de preço para dois'})
  fig.update_traces(textposition='inside', textinfo='percent')
  fig = st.plotly_chart(fig, use_container_width=True)
  return fig

#--------------Início da Estrutura lógica do código--------------------------------------
#-------------------
#Import dataset
#-------------------
df = pd.read_csv('dataset/zomato.csv')

#Limpeza dos Dados
df1 = clean_code(df)

st.set_page_config('Visão Restaurantes', layout='wide')
st.header('🛎️Visão Restaurantes')
st.markdown('___')

# =======================================
# BARRA LATERAL
# =======================================

st.sidebar.image('logo.png',width=150)
st.sidebar.markdown('# Zomato Restaurant')
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

cities_options = st.sidebar.slider(label='Selecione a quantidade de restaurantes: que deseja visualizar:',min_value=1, max_value=20, value=10)

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

#Melhores restaurantes
st.subheader(f'Os {cities_options} melhores Restaurantes')
cols = ['restaurant_id','restaurant_name','country', 'city','cuisines', 'average_cost_for_two','aggregate_rating', 'votes']
df_aux = (df1.loc[:, cols]
             .sort_values(['aggregate_rating','restaurant_id'], ascending= [False, True]))

st.dataframe(data=df_aux.head(cities_options), use_container_width=True)

st.markdown('___')

#Restaurantes com maior número de avaliações
top_votes_restaurantes(df1)

st.markdown('___')
col1, col2 = st.columns(2, gap='medium')
with col1:
  #Restaurantes que fazem entrega online
  online_delivery_restaurants(df1)

with col2:
  #Restaurantes que aceitam reservas
  table_booking_restaurants(df1)
 
