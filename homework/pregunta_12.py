"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

# Carga los datos del archivo en el formato "(xxx, (v1, v2, ..., vn))".
def load_input(file_path: str) -> list:
    """Funcion load_input"""
    files = glob.glob(file_path)
    result = {}
    for line in fileinput.input(files=files):
        splited = line.split("\t")
        for item in splited[4].strip().split(","):
            _, value = item.split(":")
            if result.get(splited[0]) is None:
                result[splited[0]] = [int(value)]
            else:
                result[splited[0]].append(int(value))
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

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sequence = load_input("files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence