"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


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
    grouper = dict()
    with open('./files/input/data.csv', 'r') as file:
        for line in file.readlines():
            code = line.strip().split('\t')[4]
            pairs = [tuple(pair.split(':')) for pair in code.split(',')]
            for key, value in pairs:
                value = int(value)
                if key not in grouper:
                    grouper[key] = [value, value]
                if value < grouper[key][0]:
                    grouper[key][0] = value
                if value > grouper[key][1]:
                    grouper[key][1] = value
    
    result = sorted(grouper.items())
    result = [(letter, *stats) for letter, stats in result]
    
    return result