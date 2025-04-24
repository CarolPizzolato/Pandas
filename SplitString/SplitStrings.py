import pandas as pd
import pandasgui as gui
#preenche valores ausentes
try:
    dados = pd.read_csv (r'dados.csv')
    moda = dados["Quantidade"].value_counts().index[0]
    dados['Quantidade'].fillna(value = moda, inplace = True)
    gui.show (dados)
    
    print ('============== dados limpo==================================')
    print (dados.head())
    print ('================================================')
    dados['ID_Pedido'].str.split('-').str[1].head()
    print ('=================depois===============================')
    #agora temos a coluna ano
    dados['Ano'] = dados['ID_Pedido'].str.split('-').str[1]
    gui.show(dados)
    print ('================================================')
except FileExistsError:
    print ("Arquivo não encontrado.")


