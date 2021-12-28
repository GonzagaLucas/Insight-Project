import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import fixed
import folium
from streamlit_folium import folium_static
import plotly.express as px
from datetime import datetime

(pd.set_option('display.float_format', lambda x: '%.3f' % x))
st.set_page_config(layout='wide')
sns.set_style('whitegrid')

def barplot(a,b, aux):
    plot = sns.barplot(x=a, y=b, data=aux, edgecolor='k', palette='flare')
    sns.despine()
    return plot

#load data

data_buy = pd.read_csv('suggested_buys.csv')
data_map = pd.read_csv('buy_map.csv')
data_sell = pd.read_csv('suggested_sell.csv')
data = pd.read_csv('houserocket_tratado.csv')

st.title('Bem Vindo ao Projeto de Insights da House Rocket')
st.write('A House Rocket, é uma imobiliária fictícia, que revende imóveis, e o lucro está na compra dos '
             'imóveis por um menor preço, e a venda por um preço acima da qual foi comprado, quanto maior a diferença '
             'entre compra e venda, maior será o lucro da empresa, para isso, foi solicitado que seja feito uma análise '
             'de dados do mercado, afim de encontrar as melhores oportunidades para empresa aumentar o seu faturamento.')

st.header('Bussisnes Question')
st.write('° Quais são os imóveis que a House Rocket deveria comprar e por qual preço ?')
st.write('° Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço ?')

st.header('Sugestões de Compra')
st.write('Afim de conseguirmos encontrar as melhores opções de compra no mercado, foi levado em questão '
             'dois fatores importantes:')

st.write('1 - Localização (ZIPCODE) do imóvel')
st.write('2 - Condição do Imóvel')

st.write('Sendo assim, segue a tabela de opções de compra com base no preço mediano do imóvel na região em questão'
             'e também com base na condição(estado de conservação do imóvel')

st.subheader('Sugestões de Imóveis Para Comprar')
st.write(data_buy)

st.subheader('Sugestões de Preço de Venda e Estação do Ano a Vender')
st.write(data_sell)



st.header('Mapa com Opções de Compra')


#filters per price
min_price = int(data_map['price'].min())
max_price = int(data_map['price'].max())

#filters per bedrooms
min_bedrooms = int(data_map['bedrooms'].min())
max_bedrooms = int(data_map['bedrooms'].max())

#filter per bathrooms
min_bathrooms = int(data_map['bathrooms'].min())
max_bathrooms = int(data_map['bathrooms'].max())

st.sidebar.header('Filtros')

f_price = st.sidebar.slider('Preço Máximo de Compra', min_price, max_price, max_price)
f_bedrooms = st.sidebar.slider('Quantidade Máxima de Quartos', min_bedrooms, max_bedrooms, max_bedrooms)
f_bathrooms = st.sidebar.slider('Quantidade Máxima de Banheiros', min_bathrooms, max_bathrooms, max_bathrooms)
f_water = st.sidebar.checkbox('Vista para o Mar', False)


# draw map
houses = data_map[(data_map['price'] <= f_price) &
                      (data_map['bedrooms'] <= f_bedrooms) &
                      (data_map['waterfront'] == f_water) &
                      (data_map['bathrooms'] <= f_bathrooms)]
fig = px.scatter_mapbox(
        houses,
        lat='lat',
        lon='long',
        color="price",
        size="price",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=10)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(height=600, margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig)


st.title('Principais Insights Para Aplicar ao Negócio')
st.subheader('1 - Imóveis com vista para água são valorizados em mais de 150%')
aux1 = data[['price', 'waterfront']].groupby('waterfront').mean().reset_index()
fig = plt.figure(figsize=(6,3))
barplot('waterfront', 'price', aux1)
st.pyplot(fig)
st.write('Aplicação ao negócio: invista em imóveis com vista para água, visto que sofrem uma constante valorização')

st.subheader('Insight 2 - Imóveis com 3 ou mais banheiros são 100% mais valorizados que imóveis com menos de 3 banheiros ')
aux_bathrooms = data[['price', 'bathrooms']].copy()
aux_bathrooms['bathrooms'] = aux_bathrooms['bathrooms'].apply(lambda x: '<3' if x <3 else '>=3' )
aux_bathrooms1 = aux_bathrooms[['price', 'bathrooms']].groupby('bathrooms').mean().reset_index()
aux_bathrooms1['difference'] = aux_bathrooms1['price'].pct_change()
fig1 = plt.figure(figsize=(6,3))
barplot('bathrooms', 'price', aux_bathrooms1)
st.pyplot(fig)
st.write('Aplicação ao negócio: investir em uma reforma para acrescentar um banheiro pode fazer com que seu'
         ' imóvel sofra uma grande valorização, podendo aumentar a margem de lucro do negócio')

st.subheader('Insight 3 - A valorização do preço do imóvel é de em média, 21% ao ano')
aux_year = data[['price', 'year']].loc[data['month'] == 5 ].copy()
aux_year1 = aux_year[['price', 'year']].groupby('year').mean().reset_index()
fig2 = plt.figure(figsize=(6,3))
barplot('year', 'price', aux_year1)
st.pyplot(fig2)
st.write('Aplicação ao negócio: não apavore ao demorar a vender um determinado imóvel, lembre-se que com o passar dos '
         'meses, ele está sendo valorizado, somente saia do plano traçado em extremo caso de urgência')

st.subheader('Insight 4 - Imóveis com 4 ou mais quartos tem uma valorização de 49% no preço de mercado')
aux_bedrooms = data[['bedrooms', 'price']].copy()
aux_bedrooms['bedrooms'] = aux_bedrooms['bedrooms'].apply(lambda x: '<= 3' if x <=3 else '>3' )
aux_bedrooms1 = aux_bedrooms[['price', 'bedrooms']].groupby('bedrooms').mean().reset_index()
fig3 = plt.figure(figsize=(6,3))
barplot('bedrooms', 'price', aux_bedrooms1).set(title='Mean Price per Bedrooms')
st.pyplot(fig3)
st.write('Aplicação ao negócio: aproveite das sugestões de compra dos imóveis com 4 quartos para fazer boas vendas'
         ' e com uma boa margem de lucro, também pode aproveitar de imóveis com 2 ou 3 quartos para reformar e '
         'valorizar o preço do imóvel perante o mercado.')

st.subheader('Insight 5 - Imóveis que nunca foram reformados são em média 40% mais baratos')
data1 = data[['yr_renovated', 'price']].copy()
data1['yr_renovated'] = data1['yr_renovated'].apply(lambda x: '1' if x !=0 else '0')
data2 = data1[['yr_renovated', 'price']].groupby('yr_renovated').mean().reset_index()
fig4 = plt.figure(figsize=(6,3))
barplot('yr_renovated', 'price', data2).set(title='Diferença de Preço de Imóvel que nunca foi reformado e ja reformado - 0,1')
st.pyplot(fig4)
st.write('Aplicação ao negócio: imóveis que nunca foram reformados tem um preço bem menor de mercado,'
         ' uma boa opção seria comprar esses imóveis, reformar incremetando pelo menos 1 quarto ou banheiro'
         'para que o preço de mercado do imóvel subisse.')