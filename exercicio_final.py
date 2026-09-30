# CRIE UM DATAFRAME com OS DADOS DO ARUIVO FUNCIONARIOS.CSV E FILTRE:
## TODOS OS FUNCIONARIOS ATIVOS NO DEPARTAMENTO DE VENDAS
## TODOS OS FUCNCIONARIOS ATIVOS COM LUCRO MAIOR DO QUE 50000
## TODOS OS FUNCIONARIOS INATIVOS
# CADA FILTRO TERA QUE SER SALVO EM UM VARIAVEL
# EXPORTAR CADA FILTRO PARA UM ARQUIVO CSV 


import pandas as pd

funcionarios = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
print(funcionarios)
print('/n')

funcionaros_ativos_vendas = funcionarios[(funcionarios['ativo'] == True) & (funcionarios['departamento'] == 'Vendas')]
print(funcionaros_ativos_vendas)
print('/n')
funcionaros_ativos_vendas.to_csv('funcionaros_ativos_vendas.csv', index=False, sep=';')

funcionarios_ativos_lucro_maior_5000 = funcionarios[(funcionarios['lucro'] > 5000) & (funcionarios['lucro'] > 5000.00)]
print(funcionarios_ativos_lucro_maior_5000)
print('/n')
funcionarios_ativos_lucro_maior_5000.to_csv('funcionarios_ativos_lucro_maior_5000.csv', index=False, sep=';')


funcionarios_inativos = funcionarios[funcionarios['ativo'] == False]
print(funcionarios_inativos)
print('/n')
funcionarios_inativos.to_csv('funcionarios_inativos.csv', index=False, sep=';')


