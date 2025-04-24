import pandas as pd
import pandasgui as gui
try:
    '''Quero pesquisar onde segmento começa com CON'''
    dados = pd.read_csv (r'dados.csv')
    
    gui.show (dados [dados.Segmento.str.startswith('Con')].head())
    gui.show (dados.Segmento.value_counts())
    
except FileNotFoundError:
    print ("Arquivo não encontrado.")


