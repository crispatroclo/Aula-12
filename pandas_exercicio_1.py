# CRIAR UM DATAFRAME COM 3 LINNHAS E 3 COLUNAS
# linhas = nome, cargo, salario

import pandas as pd
dicionario = {'NOME': ['Ada', 'Bia', 'Cid'], 'CARGO': ['plantonista', 'coringa', 'rotina'], 'SALARIO': [1900.00, 1800.00, 2000.00]}
df = pd.DataFrame(dicionario) 
print(df)

df.to_csv('exercicio_1.csv', index=False, sep=';')
