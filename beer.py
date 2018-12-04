import pandas as pd
import matplotlib as plt

data = pd.read_csv('consumo_cerveja.csv')

data.plot(y='Consumo de cerveja (litros)')
plt.pyplot.show()