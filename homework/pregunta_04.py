"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    # Crea una lista vacía para almacenar los resultados
    lista = []
    with open('files/input/data.csv', mode='r', newline="") as file:
        reader = csv.reader(file)
        dict_meses = {}
        # Itera sobre cada fila en el archivo
        for row in reader:
            # Sumariza el valor de la primera columna (índice 0)
            letra = row[0].split('\t')[0]
            mes= row[0].split('\t')[2].split('-')[1]
            # Si la letra ya está en el diccionario, incrementa su contador
            if mes in dict_meses:
                dict_meses[mes] += 1
            else:
                # Si no está, inicializa su contador en 1
                dict_meses[mes] = 1
    for letra in dict_meses.keys():
        # Convierte la cantidad a entero
        lista.append((letra, dict_meses[letra]))
    # Ordena la lista alfabéticamente por la letra
    lista.sort()
    # Convierte la cantidad a entero
    return lista

# if __name__ == '__main__':
#     print(pregunta_04())