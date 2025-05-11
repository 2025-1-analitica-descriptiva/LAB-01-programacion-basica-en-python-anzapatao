"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
                    if letra not in numero_letras[numero]:
                        # Solo agregamos la letra si no está ya en la lista
                        numero_letras[numero].append(letra)
                else:
                    # Si no está, inicializamos una nueva lista con esta letra
                    numero_letras[numero] = [letra]
    
    # Convertir el diccionario a una lista de tuplas
    resultado = []
    for numero in sorted(numero_letras.keys()):  # Ordenamos por número
        # Ordenar alfabéticamente las letras antes de agregar al resultado
        numero_letras[numero].sort()  # Esta es la línea que falta en tu código
        resultado.append((numero, numero_letras[numero]))
    
    return resultado

# if __name__ == '__main__':
#     print(pregunta_08())