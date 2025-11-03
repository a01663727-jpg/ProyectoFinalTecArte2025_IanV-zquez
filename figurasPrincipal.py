import pandas as pd
from funcionesFiguras import triangulo, rectangulo, circulo

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

for index, row in dataFile.iterrows():
    if row['FIGURA'] == 't':
        area = triangulo(row['MEDIDA1'], row['MEDIDA2'])
        print(area)
#esta funcion es para calcular el area de un triangulo b*h/2
    if row['FIGURA'] == 'c':
        area = circulo(row['MEDIDA1'])
        print(area)
#esta funcion es para calcular el area de un circulo pi*r^2
    if row['FIGURA'] == 'r':
        area = rectangulo(row['MEDIDA1'], row['MEDIDA2'])
        print(area)
#esta funcion es para calcular el area de un rectangulo b*h

