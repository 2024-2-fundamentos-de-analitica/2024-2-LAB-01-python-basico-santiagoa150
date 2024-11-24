"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

# Carga los datos del archivo en el formato "(columna 2, letra)".
def load_input(file_path: str) -> list:
    """Funcion load_input"""
    files = glob.glob(file_path)
    result = []
    for line in fileinput.input(files=files):
        splited = line.split("\t")
        result.append((int(splited[1]), splited[0]))
    return result

# Ordena los datos por la primera columna.
def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

# Reduce los datos, haciendo push de las letras asociadas a cada valor de la columna 2.
def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        if result.get(key) is None:
            result[key] = [value]
        else:
            result[key].append(value)
    return list(result.items())

# Elimina los duplicados de la segunda columna.
def delete_duplicates_on_second_column(sequence):
    return [(key, sorted(list(set(value)))) for key, value in sequence]

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
    sequence = load_input("files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    sequence = delete_duplicates_on_second_column(sequence)
    return sequence