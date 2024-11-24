"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

# Carga los datos del archivo en el formato "(xxx, 1)".
def load_input(file_path: str) -> list:
    """Funcion load_input"""
    files = glob.glob(file_path)
    result = []
    for line in fileinput.input(files=files):
        splited = line.split("\t")
        for item in splited[4].strip().split(","):
            key, _ = item.split(":")
            result.append((key, 1))
    return result

# Ordena los datos por la primera columna.
def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

# Reduce los datos, sumando la cantidad de veces que aparece cada elemento.
def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        result[key] = result.get(key, 0) + value
    return result

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
    sequence = load_input("files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence