"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    # Diccionario para almacenar los números y sus letras asociadas
    numero_letras = {}
    
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                
            # Dividir la línea por tabulaciones
            campos = line.split('\t')
            
            # Verificar que hay suficientes columnas
            if len(campos) >= 2:  # Necesitamos al menos 2 columnas
                letra = campos[0]          # Primera columna - letra
                numero = int(campos[1])    # Segunda columna - número (convertido a entero)
                
                # Si el número ya está en el diccionario, agregamos la letra a su lista
                if numero in numero_letras:
                    numero_letras[numero].append(letra)
                else:
                    # Si no está, inicializamos una nueva lista con esta letra
                    numero_letras[numero] = [letra]
    
    # Convertir el diccionario a una lista de tuplas
    resultado = []
    for numero in sorted(numero_letras.keys()):  # Ordenamos por número
        resultado.append((numero, numero_letras[numero]))
    
    return resultado

if __name__ == '__main__':
    print(pregunta_07())