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
    sequence = []
    with open('./files/input/data.csv', 'r') as file:
        for line in file.readlines():
            letter, *_, col4, col5 = line.strip().split('\t')
            col4_size = len(col4.split(','))
            col5_size = len(col5.split(','))
            sequence.append((letter, col4_size, col5_size))
    
    return sequence