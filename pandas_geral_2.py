# VISUALIZAÇÃO E FILTRAGEM

import pandas as pd

dicionario = {'NOME': ['joao', 'maria', 'pedro', 'alex', 'juliana', 'marcos'], 
              'IDADE': [12, 10, 11, 9, 13, 10],
              'NOTA': [7.0, 5.6, 9.0, 6.2, 5.7, 10]}

df = pd.DataFrame(dicionario) 
print(df)
print('\n')

# visualizar as 3 primeiras linhas
df_tres_primeiras_linhas = df.head(3)
print(df_tres_primeiras_linhas)
print('\n')

# visualizar as 3 ultimas linhas
df_tres_ultimas_linhas = df.tail(3)
print(df_tres_ultimas_linhas)
print('\n')

# filtrar notas maiores ou iguais a 7
df_nota_maior_igual_7 = df[df['NOTA'] >= 7]
print(df_nota_maior_igual_7)
print('\n')

# filtar idades menores do que 10
df_idade_menor_10 = df[df['IDADE'] < 10]
print(df_idade_menor_10)
print('\n')

# exportando o dataframa para um arquivo .csv
df.to_csv('pandas_geral_2.csv', index = False, sep=";") # sep indica qu eo simbolo ; indica a sepaçaõ entre as colunas