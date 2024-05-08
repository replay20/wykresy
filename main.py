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

#Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

grupa2 = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa2)

grupa2.plot(kind='bar', xlabel='Plec', ylabel='Liczba (mln)', rot=0, legend=True, title='Liczba urodzeń z podziałem na płeć')
plt.show()