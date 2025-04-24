import pandas as pd
import pandasgui as gui
try:
    
    dados = pd.read_csv (r'C:\Users\User\Desktop\Python DSA\Parte10\dados.csv')
    print ((dados['Data_Pedido'].str.lstrip('20'))) #quero tirar o 20
    #se tivesse 2020 ficaria sem sentido
    
except FileExistsError:
    print ("Arquivo não encontrado.")


