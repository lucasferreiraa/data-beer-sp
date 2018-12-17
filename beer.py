import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse
from datetime import datetime
import pyflux as pf
import seaborn as sns

data_beer = pd.read_csv('consumo_cerveja.csv')

#print(data_beer)
#print(data_beer.head())
#print(data_beer.columns)
#print(len(data_beer.columns))
#print(data_beer.columns[0])
#print(data_beer[0])

#Doesn't work :/
'''
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
data_beer = pd.read_csv('consumo_cerveja.csv', parse_dates=['Data'], date_parser=dateparse)
'''

data_beer = pd.read_csv('consumo_cerveja.csv', parse_dates=['Data'])
data_beer['Data'] = pd.to_datetime(data_beer['Data'], format="%d-%m-%Y")

data_beer.plot(x='Data', y='Consumo de cerveja (litros)')
plt.grid(True)
plt.ylabel('Consumo de cerveja')
plt.show()

#Deixando a série estacionária
data_beer = np.log(data_beer['Consumo de cerveja (litros)'])
data_beer_diff = data_beer - data_beer.shift()
#data_beer = data_beer['Consumo de cerveja (litros)']
plt.plot(data_beer_diff['Consumo de cerveja (litros)'])
plt.grid(True)
plt.show()

data_beer = pd.Series.to_frame(data_beer)

#ar: qtd de iterações de autorregressão; ma: qtd de iterações de médias móveis
model = pf.ARIMA(ar=9, ma=2, data=data_beer, target='Consumo de cerveja (litros)')

x = model.fit("MLE")
x.summary()
#model.plot_fit()
