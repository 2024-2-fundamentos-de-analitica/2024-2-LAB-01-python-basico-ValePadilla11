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

    counter = dict()
    with open('./files/input/data.csv', 'r') as file:
        for line in file.readlines():
            letter_list = line.split('\t')[3].split(',')
            number = int(line.split('\t')[1])
            for letter in letter_list:
                if letter not in counter:
                    counter[letter] = 0
                counter[letter] += number

    result = dict(sorted(counter.items()))

    return result