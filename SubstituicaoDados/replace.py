import pandas as pd
import pandasgui as gui
try:
    
    dados = pd.read_csv (r'C:\Users\User\Desktop\Python DSA\Parte10\dados.csv')
    dados ['ID_Cliente'] = dados ['ID_Cliente'].str.replace('CG','AX') #troquei CG por ax, ou seja onde sera cg virou ax
    gui.show (dados.head())
    
except FileExistsError:
    print ("Arquivo não encontrado.")


