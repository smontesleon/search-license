


import matplotlib.pyplot as plt 
from seaborn import load_dataset
import pandas as pd
import numpy as np
from pandas import read_csv

df = read_csv('salida.csv')
df.columns = ['CARPETA', 'ARCHIVO', 'LICENCIA']
df.to_csv('test_3.csv')



#Colocar dirección donde se generó test.csv
data=pd.read_csv('/home/sergioml/Documentos/Python/script/test_3.csv')
print (data.head(5))
print(data)
print('Cantidad de Filas y columnas:',data.shape)
print('Nombre columnas:',data.columns)
data.info()
data.describe()
data2= data.groupby(['LICENCIA']).size().reset_index(name='numero_preferencias')
print (data2)
data2.to_csv('licencias.csv')

data2.plot.bar("LICENCIA", "numero_preferencias");



