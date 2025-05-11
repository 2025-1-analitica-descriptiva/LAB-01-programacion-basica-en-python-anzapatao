"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    dict_valores = {}
    
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
                    clave, _ = item.split(':')
                    dict_valores.setdefault(clave, 0)  # Inicializa la clave si no existe
                    dict_valores[clave] += 1
                    
    dict_ordenado = dict(sorted(dict_valores.items()))
    return dict_ordenado

if __name__ == '__main__':
    print(pregunta_09())