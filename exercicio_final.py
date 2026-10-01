# CRIE UM DATAFRAME com OS DADOS DO ARUIVO FUNCIONARIOS.CSV E FILTRE:
## TODOS OS FUNCIONARIOS ATIVOS NO DEPARTAMENTO DE VENDAS
## TODOS OS FUCNCIONARIOS ATIVOS COM LUCRO MAIOR DO QUE 50000
## TODOS OS FUNCIONARIOS INATIVOS
# CADA FILTRO TERA QUE SER SALVO EM UM VARIAVEL
# EXPORTAR CADA FILTRO PARA UM ARQUIVO CSV 


import pandas as pd

funcionarios = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv") # importei o arquivo do computador 
print(funcionarios) # exibição da tabela origina
print('/n') # pula linha

funcionaros_ativos_vendas = funcionarios[(funcionarios['ativo'] == True) & (funcionarios['departamento'] == 'Vendas')] # seleciona as linhas com resposta 'verdadeiro' na coluna ativo e resposta 'vedndas' na coluna departamento
print(funcionaros_ativos_vendas) # exibe no formtao tabela as linhas e colunas selecionadas
print('/n') # pula linha
funcionaros_ativos_vendas.to_csv('funcionaros_ativos_vendas.csv', index=False, sep=';') # salva o arquivo como .csv no computador

funcionarios_ativos_lucro_maior_5000 = funcionarios[(funcionarios['ativo'] == True) & (funcionarios['lucro'] > 5000.00)] # seleciona as linhas com resposta verdadeira na coluna ativo e resposta '>5000' na coluna lucro
print(funcionarios_ativos_lucro_maior_5000) # exibe no formtao tabela as linhas e colunas selecionadas
print('/n') # pula linha
funcionarios_ativos_lucro_maior_5000.to_csv('funcionarios_ativos_lucro_maior_5000.csv', index=False, sep=';') # salva o arquivo como .csv no computador


funcionarios_inativos = funcionarios[funcionarios['ativo'] == False] # # seleciona as linhas com resposta 'falso' na coluna ativo 
print(funcionarios_inativos) # exibe no formtao tabela as linhas e colunas selecionadas
print('/n') # pula linha
funcionarios_inativos.to_csv('funcionarios_inativos.csv', index=False, sep=';') # salva o arquivo como .csv no computador


