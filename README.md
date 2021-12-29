# House Rocket - Projeto de Insights.
![image](https://user-images.githubusercontent.com/95088918/147466912-616dd1ee-43f5-42b2-b9cd-367199907bca.png)

*Esse é um projeto fictício, onde o contexto como: a empresa, CEO e questões de negócios, não são reais.
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[<img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>](https://analytics-house-gonzaga.herokuapp.com/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://analytics-house-gonzaga.herokuapp.com/)
# Bem vindo a House Rocket Sales.
A House Rocket é uma empresa fictícia, pertecente ao ramo imobiliário, se trata de uma empresa especializada na compra e venda de 
imóveis, o seu lucro consiste em comprar imóveis por um preço menor que a média do mercado, e posteriormente vender por um valor maior
que o comprado, no entanto, o cenário do mercado está cada vez mais desafiador, os imóveis possuem cada vez mais atributos, o que interfere
diretamente no valor de revenda, como por exemplo: região do imóvel, quantidade de cômodos e mês do ano em que o imóvel está sendo vendido.

Para pontecializar a quantidade de bons negócios feitos pela House Rocket, o CEO nos contactou para fazermos uma análise dos imóveis disponíveis
para compra, para que possamos encontrar as melhores opções de imóveis a investir.
  
O foco principal do projeto será responder as seguintes perguntas:
    
    ° Quais casas a House Rocket deveria comprar e por qual preço de compra?
    ° Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?
    
# Atributos.

Os dados para esse projeto foram coletados na plataforma do Kaggle: https://www.kaggle.com/harlfoxem/housesalesprediction

Nesse conjunto de dados está listadas as casas a venda em King County - USA, entre os anos de 2014 e 2015
|    Atributos    |                         Definição                            |
| :-------------: | :----------------------------------------------------------: |
|       id        |       Numeração única de identificação de cada imóvel        |
|      date       |                    Data da venda do imóvel                   |
|      price      |    Preço que o imóvel foi colocado a venda                   |
|    bedrooms     |                      Número de quartos                       |
|    bathrooms    | Número de banheiros (0.5 = banheiro sem chuveiro)            |
|   sqft_living   | Medida (em pés quadrado) do espaço interior dos apartamentos |
|    sqft_lot     |     Medida (em pés quadrado) quadrada do espaço terrestre     |
|     floors      |                 Número de andares do imóvel                  |
|   waterfront    | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) |
|      view       | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa  4 = alta |
|    condition    | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde: 1 = baixo \|-\| 5 = alta |
|      grade      | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta |
|  sqft_basement  | A metragem quadrada do espaço habitacional interior acima do nível do solo |
|    yr_built     |               Ano de construção de cada imóvel               |
|  yr_renovated   |                Ano de reforma de cada imóvel                 |
|     zipcode     |                         CEP da casa                          |
|       lat       |                           Latitude                           |
|      long       |                          Longitude                           |
| sqft_livining15 | Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo |
|   sqft_lot15    | Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo |

# Premissas Assumidas.

  Consideramos as premissas para o projeto:
  - Valores de "ID" duplicados foram excluídos.
  - A coluna "price" representa o valor de compra do imóvel.
  - Dividimos o calendário em uma nova coluna, chamada "season", onde o valor da coluna é a estação do ano da data do anúncio, uma vez que se trata de uma informação relevante para precificar o imóvel.

# Processo de Solução.

1 - Coleta dos dados em seu local de origem (Kaggle)

2 - Entendimento do negócio

3 - Limpeza e tratamento do DF
    
      Checagem de outliers impactantes no resultado final
      Transformação de variáveis que apresentavam o tipo errado
      Limpeza de valores duplicados

4 - Análise exploratória dos dados

5 - Criação de hipóteses para extração de insights para o negócio

6 - Criação do web app com dashboards de auxílio a tomada de decisão da companhia

7 - Conclusão

       Resultado financeiro do projeto
       Considerações finais
       
# Principais Insights e Forma de Aplicação

| Insights                                                     |  Aplicação                                                   |
| ------------------------------------------------------------ |  ------------------------------------------------------------ |
| **1** - Imóveis com vista para água são valorizados em mais de 150% | Investir em imóveis com vista para água                      |
| **2** - Imóveis com 3 ou mais banheiros são 100% mais valorizados que imóveis com menos de 3 banheiros | Investir em imóveis com pelo menos dois banheiros, e a depender da situação do imóvel, adicionar um banheiro       |
| **3** - A valorização do preço do imóvel é de, em média, 21% ao ano | Não desespere se determinado imóvel ficar alguns dias, ou meses, a venda, lembre-se que esse imóvel está sendo valorizado, e se for o caso, reajuste o preço de venda de acordo com a valorização                         |
| **4** - Imóveis com 4 ou mais quartos tem uma valorização de 49% no preço de mercado | Investir em imóveis com 3 quartos e fazer uma reforma pode aumentar ainda mais o preço desse imóvel no mercado  |
| **5** - Imóveis que nunca foram reformados são em média 40% mais baratos | Investir em imóveis não reformados, e posteriormente reforma-los para vender, duas sugestões de reformas com base nos dados que valorizará o imóvel: adicionar banheiro e quarto                         |


# Retorno Financeiro Obtido e Conclusão

Após a análise exploratória dos dados, a fim de potencializarmos o ROI da House Rocket, e gerar mais resultados financeiros para a mesma, podemos dizer que nosso projeto foi concluído com sucesso, finalizamos uma tabela contendo sugestões de compra de imóveis para a House Rocket com base no preço mediano dos imóveis daquela região, e para que não fosse comprado imóveis em baixa condição de conservação, usamos também filtros que selecionaram apenas imóveis conservados.

Elaboramos também uma tabela que continha sugestões de venda para os potenciais imóveis comprados, onde nessa tabela, o CEO encontraria: preço sugerido para a venda, melhor epóca do ano a se vender o imóvel, e lucro esperado pela transação, através dessa tabela, o CEO conseguiria explorar o potencial de venda do imóvel.

Por ultimo, finalizamos um APP que foi colocado em produção(disponível para o CEO acessar em qualquer lugar, seja de um computador, tablet, ou celular), e nesse APP ele conseguria ter acesso a essas duas tabelas em apenas um lugar, além de poder visualizar no mapa interativo os imóveis sugeridos para compra, e também pesquisar imóveis por atributos específicos.

O lucro resultante da venda dos imóveis está estipulado em *$376.310.918,50*, deixando assim claro, que se o time de negócios da empresa souber utilizar os insights aqui apresentados, juntamente das sugestões de compra, a House Rocket terá um ótimo retorno financeiro!


