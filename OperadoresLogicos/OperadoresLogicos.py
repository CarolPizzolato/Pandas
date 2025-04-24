import pandas as pd

try:
    
    dados = pd.read_csv (r'dados.csv')
    #filtrando dados
    print ("===================  dados igual a: e head ================================================")
    print(dados [(dados.Segmento == 'Home Office') & (dados.Regiao == 'South')].head()) #5 primeiras
    print ("==================== dados ou e tail   ===============================================")
    print (dados [(dados.Segmento == 'Home Office') | (dados.Regiao == 'South')].tail()) #ultimas linhas 
    print ("==================== dados != e sample ==============================================")
    print (dados [(dados.Segmento != 'Home Office') & (dados.Regiao != 'South')].sample()) #.sample pega linha aleatória
    print ("===================================================================")

    
except FileNotFoundError:
    print ("Arquivo não encontrado.")


