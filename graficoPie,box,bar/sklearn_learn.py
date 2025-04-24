from sklearn.datasets import load_iris
import pandas as pd
import pandasgui as gui
import matplotlib.pyplot as plt
data = load_iris()
data_f = pd.DataFrame(data['data'], columns = data['feature_names'])
data_f ['species'] = data['target']

data_f.groupby('species').mean().plot.bar() #grafico barra
plt.show()

data_f.groupby('species').count().plot.pie(y= 'sepal length (cm)') #grafico pizza
plt.show()

columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
data_f[columns].plot.box(figsize = (8,8)) #grafico box (parece umas seringa)
plt.show()
