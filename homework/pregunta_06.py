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
            key, value = item.split(":")
            if result.get(key) is None:
                result[key] = [int(value)]
            else:
                result[key].append(int(value))
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
        result.append((key, min(value),  max(value)))
    return result

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
    sequence = load_input("files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence