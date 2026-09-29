# crie dataframe a partit do dicionario e faça os seguintes filtros
# funcionario com salario maior do que 3000,00
# funcionarios com cargo de vendador

import pandas as pd

dicionario = {'nome': ['geronimo', 'martha', 'patroclos', 'tiberios', 'janaina', 'mercedes'],
              'cargo': ['gerente', 'gerente', 'vendedor', 'secretario', 'vendedora', 'vendedor'],
              'salario': [9600.56, 9600.56, 2600.90, 4500.45, 2600.90, 2600.90]}

df = pd.DataFrame(dicionario)
print(df)
print('\n')

df_salario_maior_3000 = df[df['salario'] > 3000.00] 
print(df_salario_maior_3000)
print('\n')

df_cargo_vendedor = df[(df['cargo'] == 'vendedor') | (df['cargo'] == 'vendedora')]
print(df_cargo_vendedor)
print('\n')

df.to_csv('exercicio_2.csv', index=False, sep=';')
df_salario_maior_3000.to_csv('df_salario_maior_3000.csv', index=False, sep=';')
df_cargo_vendedor.to_csv('df_cargo_vendedor.csv', index=False, sep=';')