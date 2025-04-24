import pandas as pd
from pandas import DataFrame as df #faz a tabela
import pandasgui as gui
import numpy as np
dicionario = {  'Estado': ['sc','rs','mg'], 'ano':[2000,2001,2002], 'desemprego': [0.3,4.5,3.1]}

#Dat é o primeiro dataframe
dat = df(dicionario)
print (df.head(dat))

#acrescenta uma coluna taxa crescimento
data2 = pd.DataFrame ( dicionario,
            columns = ['Estado', 'desemprego', 'taxa crescimento', 'ano'], #adiciona mais uma colina de tx cresc
            index = ['estado1','estado2','estado3']) #adiciona uma coluna de estado1
print ("============== ANTES==============================================")

print (data2.isna()) #se está vazia TRUE OR FALSE
print ("============================================================")


data2 ['taxa crescimento'] = np.arange(3.)

print ("============== DEPOIS==============================================")
print (data2.isna()) #foi completado, agora tem que dar Null todos

print ("============================================================")

print (data2)
gui.show(data2)