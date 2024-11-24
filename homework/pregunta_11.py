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
        for item in splited[3].strip().split(","):
            if result.get(item) is None:
                result[item] = [int(splited[1])]
            else:
                result[item].append(int(splited[1]))
    return list(result.items())

# Ordena los datos por la primera columna.
def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

# Reduce los datos, sumando la cantidad de veces que aparece cada elemento.
def reducer(sequence):
    """Reducer"""
    result = {}
    for key, values in sequence:
        result[key] = result.get(key, 0) + sum(values)
    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sequence = load_input("files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence