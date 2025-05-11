"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Abre el archivo CSV
    with open('files/input/data.csv', mode='r') as file:
        reader = csv.reader(file)
        suma = 0
        # Itera sobre cada fila en el archivo
        for row in reader:
            # Suma el valor de la segunda columna (índice 1)
            suma += int(row[0].split('\t')[1])
        
    return suma

if __name__ == '__main__':
    pregunta_01()