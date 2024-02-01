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

def restaurant_maps(df1):
  cols = ['restaurant_name','average_cost_for_two','cuisines','aggregate_rating','city','latitude', 'longitude', 'rating_color']

  map = folium.Map()

  marker_cluster = MarkerCluster().add_to(map)

  for index,line in df1.iterrows():

    name = line["restaurant_name"]
    price_for_two = line["average_cost_for_two"]
    cuisine = line["cuisines"]
    currency = line["currency"]
    rating = line["aggregate_rating"]
    color = f'{line["rating_color"]}'

    html = "<p><strong>{}</strong></p>"
    html += "<p>Price: {},00 ({}) para dois"
    html += "<br />Type: {}"
    html += "<br />Aggragate Rating: {}/5.0"
    html = html.format(name, price_for_two, currency, cuisine, rating)

    popup = folium.Popup(
              folium.Html(html, script=True),
              max_width=500,
    )

    folium.Marker([line['latitude'],
                  line['longitude']],
                  popup=popup,
                  icon=folium.Icon(color=line['rating_color'],
                  icon='home')).add_to(marker_cluster)

  folium_static(map, width=1024, height=600)


#--------------Início da Estrutura lógica do código--------------------------------------
#-------------------
#Import dataset
#-------------------
df = pd.read_csv('dataset/zomato.csv')

#Limpeza dos Dados
df1 = clean_code(df)

st.set_page_config('Visão Geral', layout='wide')
st.header('⚙️Visão Geral & Geográfica')
st.markdown('___')
st.subheader('Overall Metrics')

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

country_options = st.sidebar.multiselect(options=lista_paises, label='Selecione os países que deseja analisar:', 
                                         default=["Australia", "Brazil", "England", "India", "South Africa", "United States of America"])

st.sidebar.markdown('___')

st.sidebar.markdown('## Dados tratados:')
st.sidebar.download_button(label='Download', data='dataset/zomato.csv')
st.sidebar.markdown('___')
st.sidebar.markdown('###### Powered by Marcos Paulo | mpcruz®')

# =======================================
# LAYOUT PRINCIPAL NO STREAMLIT
# =======================================

#Filtro de trânsito
linhas_selecao = df1['country'].isin(country_options)
df1 = df1.loc[linhas_selecao, :]

with st.container():
  col1, col2, col3, col4, col5 = st.columns(5, gap='small')
  with col1:
      rest_unicos = df1['restaurant_id'].nunique()
      col1.metric('Restaurantes registrados:',rest_unicos)

  with col2:
      pais_unicos = (df1['country'].nunique())
      col2.metric('Países cadastrados:',pais_unicos)

  with col3:
      cid_unicos = (df1['city'].nunique())
      col3.metric('Cidades cadastradas:',cid_unicos)

  with col4:
      tot_aval = df1['votes'].sum()
      col4.metric('Total de Avaliações:',tot_aval)

  with col5:
      tot_culi = df1['cuisines'].nunique()
      col5.metric('Tipos de Culinária:',tot_culi)
st.markdown('___')

st.subheader('Encontre o Restaurante mais próximo:')

restaurant_maps(df1)