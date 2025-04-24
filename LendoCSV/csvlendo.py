import pandas as pd
#coloca valor moda onde ta vazio
try:
    
    dados = pd.read_csv ('dados.csv')
    moda = dados["Quantidade"].value_counts().index[0]
    dados['Quantidade'].fillna(value = moda, inplace = True)
    print ("itens faltando:", dados.isna().sum())
    
except FileExistsError:
    print ("Arquivo não encontrado.")


