"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

# Carga los datos del archivo en el formato "(letra, (v1, v2, ..., vn))".
def load_input(file_path: str) -> list:
    """Funcion load_input"""
    files = glob.glob(file_path)
    result = {}
    for line in fileinput.input(files=files):
        splited = line.split("\t")
        if result.get(splited[0]) is None:
            result[splited[0]] = [int(splited[1])]
        else:
            result[splited[0]].append(int(splited[1]))
    return list(result.items())

# Ordena los datos por la primera columna.
def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

# Reduce los datos, obteniendo el valor maximo y minimo por cada letra.
def reducer(sequence):
    """Reducer"""
    result = []
    for key, value in sequence:
        result.append((key, max(value), min(value)))
    return result

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    sequence = load_input("files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence