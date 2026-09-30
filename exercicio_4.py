import pandas as pd

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
print(df)
print('\n')

df_funcionarios_com_lucro_ativo = df[(df['lucro'] != 0) & (df['ativo'] == True)]
print(df_funcionarios_com_lucro_ativo)