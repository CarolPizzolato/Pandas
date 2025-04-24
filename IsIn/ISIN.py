import pandas as pd

try:
    
    dados = pd.read_csv (r'C:\Users\User\Desktop\Python DSA\Parte10\dados.csv')
    print (dados [dados ['Quantidade'].isin([5,7,9,11])])
    print (dados [dados ['Quantidade'].isin([5,7,9,11])].shape)
    
    
except FileNotFoundError:
    print ("Arquivo não encontrado.")


