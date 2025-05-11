"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    # Crea un diccionario vacío para almacenar los resultados
    dict_valores = {}  # Cambiado de lista a diccionario
    
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            line = line.strip()
            # Salta líneas vacías
            if not line:
                continue
            
            # Divide la línea por tabulaciones
            campos = line.split('\t')
            
            # Verifica que hay suficientes columnas
            if len(campos) >= 5:
                col5 = campos[4].split(',')
                for item in col5:
                    if not item:  # Salta elementos vacíos
                        continue
                    
                    # Separa la clave y el valor
                    clave, valor = item.split(':')
                    # Convierte el valor a entero
                    valor = int(valor)
                    
                    # Si la clave ya está en el diccionario, actualiza máximo y mínimo
                    if clave in dict_valores:
                        # Actualiza el máximo si el valor es mayor
                        if valor > dict_valores[clave]['max']:
                            dict_valores[clave]['max'] = valor
                        # Actualiza el mínimo si el valor es menor
                        if valor < dict_valores[clave]['min']:
                            dict_valores[clave]['min'] = valor
                    else:
                        # Si no está, inicializa su máximo y mínimo
                        dict_valores[clave] = {'min': valor, 'max': valor}
    
    # Convertir el diccionario a la lista de tuplas requerida
    resultado = []
    for clave in dict_valores:
        resultado.append((clave, dict_valores[clave]['min'], dict_valores[clave]['max']))
    
    # Ordenar la lista alfabéticamente por clave
    resultado.sort()
    
    return resultado
            
# if __name__ == '__main__':
#     print(pregunta_06())