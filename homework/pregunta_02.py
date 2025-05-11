"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    # Crea una lista vacía para almacenar los resultados
    lista = []
    with open('files/input/data.csv', mode='r', newline="") as file:
        reader = csv.reader(file)
        dict_letras = {}
        # Itera sobre cada fila en el archivo
        for row in reader:
            # Sumariza el valor de la primera columna (índice 0)
            letra = row[0].split('\t')[0]
            # Si la letra ya está en el diccionario, incrementa su contador
            if letra in dict_letras:
                dict_letras[letra] += 1
            else:
                # Si no está, inicializa su contador en 1
                dict_letras[letra] = 1
    for letra in dict_letras.keys():
        # Convierte la cantidad a entero
        lista.append((letra, dict_letras[letra]))
    # Ordena la lista alfabéticamente por la letra
    lista.sort()
    # Convierte la cantidad a entero
    return lista

# if __name__ == '__main__':
#     print(pregunta_02())