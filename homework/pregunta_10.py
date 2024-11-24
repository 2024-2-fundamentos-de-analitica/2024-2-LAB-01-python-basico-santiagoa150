"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

# Carga los datos del archivo en el formato "(letra, "x,x,x", "xxx:1,xxx:2")".
def load_input(file_path: str) -> list:
    """Funcion load_input"""
    files = glob.glob(file_path)
    result = []
    for line in fileinput.input(files=files):
        splited = line.split("\t")
        result.append((splited[0], splited[3], splited[4]))
    return result

# Reduce los datos, sumando la cantidad de veces que aparece cada elemento.
def reducer(sequence):
    """Reducer"""
    result = []
    for key, column4, column5 in sequence:
        result.append((key, len(column4.split(",")), len(column5.split(","))))
    return result


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
    sequence = load_input("files/input/data.csv")
    sequence = reducer(sequence)
    return sequence