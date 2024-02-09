#Libraries
import pandas as pd
import inflection
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

def best_cuisines_type(df1):
  melhores_restaurantes_por_tipo = df1.groupby('cuisines').apply(
  lambda x: x.nlargest(1, 'aggregate_rating')).reset_index(drop=True)

  # Divida o DataFrame em partes iguais para cada coluna
  partes = [melhores_restaurantes_por_tipo.iloc[i:i+5]
              for i in range(0, len(melhores_restaurantes_por_tipo), 5)]

  # Para cada parte, criar uma coluna na grade
  for parte in partes:
      colunas = st.columns(5)
      for idx, (_, row) in enumerate(parte.iterrows()):
          with colunas[idx]:
              label = f"{row['cuisines']}: {row['restaurant_name']}"
              value = f"{row['aggregate_rating']}/5.0"
              info_adicional = f"**País:** {row['country']}  \n**Cidade:** {row['city']}  \n**Preço para duas pessoas:** {row['currency']}{row['average_cost_for_two']}"
              st.metric(label=label, value=value, help=info_adicional)

def best_restaurants_cost_for_two(df1):  
  colunas=['city', 'country', 'average_cost_for_two', 'cuisines', 'currency']
          
  df_aux=(df1.loc [:,colunas]
            .groupby(['country', 'city', 'cuisines', 'currency'])
            .max()
            .sort_values('average_cost_for_two', ascending=False)
            .reset_index())

  df = st.dataframe(df_aux.head(culinarias_options), use_container_width=True)
  return df

def top_cuisines_online_delivery(df1):
  lines = (df1['has_online_delivery'] == 1) & (df1['is_delivering_now'] == 1)

  df_aux = (df1.loc[lines, ['restaurant_id', 'cuisines'] ]
              .groupby('cuisines')
              .count()
              .sort_values('restaurant_id', ascending=False)
              .reset_index())

  fig = px.bar(df_aux, x='cuisines', y='restaurant_id',
              labels={'cuisines':'Tipos de Culinária', 'restaurant_id':'Quantidade de restaurantes'},
              text_auto='restaurant_id')

  graf = st.plotly_chart(fig, use_container_width=True, )
  return graf

#--------------Início da Estrutura lógica do código--------------------------------------
#-------------------
#Import dataset
#-------------------
df = pd.read_csv('dataset/zomato.csv')

#Limpeza dos Dados
df1 = clean_code(df)

st.set_page_config('Visão Culinaria', layout='wide')
st.header('🍽️Visão Culinária')
st.markdown('___')

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

culinarias_options = st.sidebar.slider(label='Selecione a quantidade de culinárias: que deseja visualizar:',min_value=1, max_value=20, value=10)

cuisines = st.sidebar.multiselect(
        "Escolha os Tipos de Culinária ",
        df1.loc[:, "cuisines"].unique().tolist(),
        default=[
            "BBQ",
            "Japanese",
            "Brazilian",
            "American",
            "Italian",
        ],
    )

st.sidebar.markdown('___')

st.sidebar.markdown('## Dados tratados:')
st.sidebar.download_button(label='Download', data='dataset/zomato.csv')
st.sidebar.markdown('___')
st.sidebar.markdown('###### Powered by Marcos Paulo | mpcruz®')

#Filtro de trânsito
linhas_selecao = df1['country'].isin(country_options) & df1['cuisines'].isin(cuisines)
df1 = df1.loc[linhas_selecao, :]

# =======================================
# LAYOUT PRINCIPAL NO STREAMLIT
# =======================================

#Melhores restaurantes
st.subheader('Os Melhores restaurantes dos principais tipos de culinária')
best_cuisines_type(df1)
st.markdown('___')

#Melhores restaurantes com o preço médio para duas pessoas
st.write(f'#### As {culinarias_options} maiores culinárias com preço médio de um prato para duas pessoas\n')
best_restaurants_cost_for_two(df1)
st.markdown('___')

#Culinárias que aceitam pedidos online e fazem entregas
st.write(f'#### Tipos de culinária que mais possuem restaurantes que aceitam pedidos online e fazem entregas\n')  
top_cuisines_online_delivery(df1)
