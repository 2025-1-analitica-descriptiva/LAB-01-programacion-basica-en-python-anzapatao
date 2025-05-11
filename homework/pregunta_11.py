"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
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
                valor_col2 = int(campos[1])  # Segunda columna - valor
                letras_col4 = campos[3].split(',')  # Cuarta columna - lista de letras
                
                # Para cada letra en la columna 4
                for letra in letras_col4:
                    # Sumar el valor de la columna 2 a la letra correspondiente
                    if letra in resultado:
                        resultado[letra] += valor_col2
                    else:
                        resultado[letra] = valor_col2
    
    # Ordenar el diccionario por las claves (letras)
    resultado = dict(sorted(resultado.items()))
    
    return resultado
if __name__ == '__main__':
    print(pregunta_11())