"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    group_counter = dict()
    with open('./files/input/data.csv', 'r') as file:
        for line in file.readlines():
            letter = line.split('\t')[0]
            value = int(line.split('\t')[1])
            if letter not in group_counter:
                group_counter[letter] = 0
            group_counter[letter] += value
    
    result = sorted(group_counter.items(), key=lambda x: x[0])

    return result