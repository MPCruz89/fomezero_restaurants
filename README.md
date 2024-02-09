### 1.PROBLEMA DE NEGÓCIO
___

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:

**VISÃO GERAL**

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

**VISÃO PAÍSES**

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

**VISÃO CIDADES**

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
Conteúdo licenciado para Marcos Paulo Dias da Cruz - 361.464.348-41
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

**VISÃO RESTAURANTES**

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os
restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
possuem um valor médio de prato para duas pessoas maior que as churrascarias
americanas (BBQ)?

**VISÃO TIPOS DE CULINÁRIAS**

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
online e fazem entregas?

### 1.PREMISSAS ASSUMIDAS PARA A ANÁLISE
___

1. Marketplace foi o modelo de negócio assumido.
2. As principais visões do negócio foram: Visão por País, Visão por Cidades, Visão Restaurantes e Visão por Tipo de Culinárias.

**ESTRATÉGIAS DE SOLUÇÃO**

O painel estratégico foi desenvolvido utilizando as métricas que refletem as principais visões do modelo de negócio da empresa:

1. Visão por Países;
2. Visão por Cidades;
3. Visão por Restaurantes;
4. Visão por Tipos de Culinárias;

Dispomos na página inicial as informações gerais com opção de seleção de Filtro por país com as informações gerais do Marketplace, além de uma mapa interativo, em que é possível identificar a localização de cada restaurante com rank de cores e suas principais características (Valor prato para dois, Tipo de Culinária e Nota Média de avaliação)

Cada visão é representada pelo seguinte conjunto de métricas.

Visão Geral:

Quantidade de Restaurantes cadastrados

Quantidade de Países;

Quantidade de Cidades registradas;

Total de avaliações realizadas;

Quantidade de tipos de culinárias cadastrados;

Mapa com a localização de cada restaurante

Visão por País:

Quantidade de Restaurantes registrados por país;

Quantidade de Cidades registradas por país;

Média de avaliações por país;

Média de preço de um prato para duas pessoas por país;

Visão por Cidade:

Top 10 Cidades com mais restaurantes registrados;

Top 10 Cidades com mais restaurantes com média maior que 4;

Top 10 Cidades com mais restaurantes com média menor que 2.5;

Top 10 Cidades com mais tipos de culinárias distintos;

Top 10 Cidades com maiores valores de prato para duas pessoas;

Visão por Restaurantes:

Os 10 melhores restaurantes;

Top 10 restaurantes com maior número de avaliações;

Percentual de restaurantes que realizam entregas;

Percentual de restaurantes que aceitam reservas;

Visão por Tipo de Culinária:

Melhores restaurantes dos principais tipos de culinárias;

Top 10 melhores culinárias contendo o preço médio de um prato para duas pessoas

Tipos de culinária que mais possuem restaurantes que realizam entregas

**TOP 3 INSIGHTS:**

A Índia possui a maior quantidade de restaurantes e, ao mesmo tempo, os melhores restaurantes cadastrados na plataforma;

Os restaurantes que realizam entrega recebem duas vezes mais avaliações do que aqueles que não entregam seus pratos;

A Austrália possui somente 180 restaurantes registrados, contudo, é o 3º país que mais recebe avaliações. Ou seja, os clientes têm o hábito de avaliarem seus pedidos.

**Produto Final**
Dashboard online, hospedado no Streamlit Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado através desse link: [https://fomezero-well.streamlit.app/](https://fomezero-mpcruz.streamlit.app/visao_paises)

**Conclusão**
O objetivo deste Projeto é criar um painel online, composto de um conjunto de gráficos e/ou tabelas que exibam as métricas de negócio da melhor forma possível para o CEO acompanhar o crescimento da empresa.

**Próximo passos**
Reduzir o número de métricas;

Criar novos filtros conforme demanda do CEO;

Dispor de features com as informações dos clientes (Sexo, Idade);

Criar uma feature com conversão dos valores dos pratos para moeda única, a fim de padronizar os valores;

Adicionar novas visões de negócio (Visão Clientes, por exemplo)
