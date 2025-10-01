""" Este programa tiene como proposito crear un generador que devuelva todas las permutaciones de una lista una a una """

def permutaciones(lista):
    """ Funcion para generar las permutaciones """
    if len(lista) == 0:
        return [[]]
    resultado = []
    for i in range(len(lista)):
        primero = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones(resto):
            resultado.append([primero] + p)
    return resultado

def generar_permutaciones(lista):
    """ Este es el generador en si """

    for permutacion in permutaciones(lista):
        yield permutacion

# Prueba
mi_lista = [1, 2, 3, 4, 5]

for p in generar_permutaciones(mi_lista):
    print(p)