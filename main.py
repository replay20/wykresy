import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik, header=0)
print(df)

grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(grupa)

grupa.plot()
plt.show()

