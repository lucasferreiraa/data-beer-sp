import pandas as pd
import matplotlib as plt

data = pd.read_csv('consumo_cerveja.csv')

#dataparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
data = pd.read_csv('consumo_cerveja.csv', parse_dates=['Data']) #date_parser=dataparse)
data['Data'] = pd.to_datetime(data['Data'], format="%d-%m-%Y")

data.plot(x= 'Data', y='Consumo de cerveja (litros)')
plt.pyplot.show()
