'''Abrindo o arquivo para teste'''
import pandas as pd
import pandasgui as gui
try:
    
    dados = pd.read_csv (r'dados.csv')
    gui.show (dados [['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).agg(['mean','std','count']))
    
    
except FileNotFoundError:
    print ("Arquivo não encontrado.")


