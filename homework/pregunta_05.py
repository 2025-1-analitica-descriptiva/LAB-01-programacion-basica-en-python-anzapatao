"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    # Crea una lista vacía para almacenar los resultados
    lista = []
    with open('files/input/data.csv', mode='r', newline="") as file:
        reader = csv.reader(file)
        dict_letras = {}
        # Itera sobre cada fila en el archivo
        for row in reader:
            # Separa la línea por tabulaciones
            campos = row[0].split('\t')
            letra = campos[0]
            cantidad = int(campos[1])
            
            # Si la letra ya está en el diccionario, actualiza máximo y mínimo
            if letra in dict_letras:
                # Actualiza el máximo si la cantidad es mayor
                if cantidad > dict_letras[letra]['max']:
                    dict_letras[letra]['max'] = cantidad
                # Actualiza el mínimo si la cantidad es menor
                if cantidad < dict_letras[letra]['min']:
                    dict_letras[letra]['min'] = cantidad
            # Si la letra no está en el diccionario, inicializa
            else:
                dict_letras[letra] = {'min': cantidad, 'max': cantidad}
                
    # Construye la lista de tuplas (letra, max, min)
    for letra in dict_letras:
        lista.append((letra, dict_letras[letra]['max'], dict_letras[letra]['min']))
    
    # Ordena la lista alfabéticamente por la letra
    lista.sort()
    
    return lista

if __name__ == '__main__':
    print(pregunta_05())