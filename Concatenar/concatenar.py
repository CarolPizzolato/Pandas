import pandas as pd
import pandasgui as gui
'''concatenar coluna'''
try:
    
    dados = pd.read_csv (r'dados.csv')
    dados['Pedido_Segmento'] = dados ['ID_Pedido'].str.cat (dados['Segmento'],sep = '-')
    gui.show(dados)
except FileExistsError:
    print ("Arquivo não encontrado.")


