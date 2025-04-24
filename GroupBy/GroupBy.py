import pandas as pd
import pandasgui as gui
try:
    #filtrar
    dados = pd.read_csv (r'dados.csv')
    gui.show (dados [['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).max())
    
    
except FileNotFoundError:
    print ("Arquivo não encontrado.")


