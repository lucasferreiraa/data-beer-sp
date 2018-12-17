import pandas as pd
import numpy as np

data = pd.read_csv('consumo_cerveja.csv')

data.dropna(inplace=True)
print(data.isnull().sum())
