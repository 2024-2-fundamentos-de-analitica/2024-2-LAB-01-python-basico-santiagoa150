"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

# Carga los datos del archivo en el formato "(mes, quantity)".
def load_input(file_path: str) -> list:
    """Funcion load_input"""
    files = glob.glob(file_path)
    result = []
    for line in fileinput.input(files=files):
        splited = line.split("\t")
        result.append((splited[2].split('-')[1], 1))
    return result

# Ordena los datos por la primera columna.
def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

# Reduce los datos, sumando la cantidad de veces que aparece cada mes.
def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        result[key] = result.get(key, 0) + value
    return list(result.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    sequence = load_input("files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence