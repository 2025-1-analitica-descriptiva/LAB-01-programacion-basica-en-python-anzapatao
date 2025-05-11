"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    resultado = []
    
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                
            # Dividir la línea por tabulaciones
            campos = line.split('\t')
            
            # Verificar que hay suficientes columnas
            if len(campos) >= 5:  # Necesitamos al menos 5 columnas
                letra = campos[0]          # Primera columna - letra
                col4_items = campos[3].split(',')  # Cuarta columna - lista de items
                col5_items = campos[4].split(',')  # Quinta columna - lista de items
                
                # Contar los elementos en cada columna
                col4_count = len(col4_items)
                col5_count = len(col5_items)
                
                # Añadir la tupla al resultado
                resultado.append((letra, col4_count, col5_count))
    
    return resultado

if __name__ == '__main__':
    print(pregunta_10())