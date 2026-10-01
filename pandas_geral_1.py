# BIBLIOTECA (PACKAGE)
# ex: math, pandas
# instalação: pip install nome_biblioteca
# chamamento da função: import nome_biblioteca as apelido
## pandas = pd

# Pandas
# criar estuturas de dados do zero
# lê cvs e excel
# visualiza e entende tendencias
# filtra, cruza e calcula
# salva resltados 
# checar documento disponibilizado pelo professor com os comandos
# como usar: pd.comando_desejado
# salva dados em linha e colunas:
## serie: 1 coluna
## dataframe: coleção de linhas e colunas, uma tabela
## index : numeração das linhas da coluna, podendo ser substituido por um nome para a linha
## value: cabeçalho da coluna
## ex:

import pandas as pd # importar pandas com apelido pd
dicionario = {"nome":['joão', 'maria', 'pedro'], 'idade':[12, 10, 11], 'nota':[7.0, 5.6, 9.0]} # criação do dicionario
df = pd.DataFrame(dicionario) # importa o dicionario para um dataframe
print(df) # mostra o dataframe no temrinal      

df.to_csv('pandas_geral_1.csv', index = False, sep=';')