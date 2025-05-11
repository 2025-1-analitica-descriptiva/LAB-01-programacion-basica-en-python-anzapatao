"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    resultado = {}
    
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            # Dividir la línea por tabulaciones
            campos = line.split('\t')
            
            # Verificar que hay suficientes columnas
            if len(campos) >= 4:  # Necesitamos al menos 4 columnas
                letra = str(campos[0])  # Segunda columna - valor
                letras_col4 = campos[4].split(',')  # Cuarta columna - lista de letras
                for elements in letras_col4:
                    _, value =elements.split(':')
                    value= int(value)
                    # Sumar el valor de la columna 2 a la letra correspondiente
                    if letra in resultado:
                        resultado[letra] += value
                    else:
                        resultado[letra] = value
    
    # Ordenar el diccionario por las claves (letras)
    resultado = dict(sorted(resultado.items()))
    
    return resultado

if __name__ == '__main__':
    print(pregunta_12())