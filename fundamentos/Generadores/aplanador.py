def aplanador(lista):
    """ Funcion generadora que dada una lista anidada la aplana.

        Ej: [1, [2, [3]]] -> [1, 2, 3] """

    for elemento in lista:
        if isinstance(elemento, (list, tuple)): # Comprobamos si el elemento es una coleccion (lista o tupla)
            yield from aplanador(elemento) # Llamada recursiva para delegar la tarea
        else:
            yield elemento

# Prueba
lista_anidada = [1, [2, [3, 4]], 5]
lista_aplanada = list(aplanador(lista_anidada))

print(lista_aplanada)