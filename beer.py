import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse
from datetime import datetime

data_beer = pd.read_csv('consumo_cerveja.csv')

#print(data_beer)
#print(data_beer.head())
#print(data_beer.columns)
#print(len(data_beer.columns))
#print(data_beer.columns[0])
#print(data_beer[0])

#Dosen't work :/
"""
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
data_beer = pd.read_csv('consumo_cerveja.csv', parse_dates=['Data'], date_parser=dateparse)


data_beer = pd.read_csv('consumo_cerveja.csv', parse_dates=['Data'])
data_beer['Data'] = pd.to_datetime(data_beer['Data'], format="%d-%m-%Y")

print(data_beer.head())

data_beer = data_beer.set_index('Data')

data_beer.plot(x='Data', y='Consumo de cerveja (litros)')
plt.grid(True)
plt.ylabel('Consumo de cerveja')
plt.show()
"""

#Deixando a série estacionária
data_beer = np.log(data_beer['Consumo de cerveja (litros)'])
data_beer_diff = data_beer - data_beer.shift()
plt.plot(data_beer_diff)
plt.grid(True)
plt.show()
