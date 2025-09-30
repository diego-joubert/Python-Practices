def generador_inverso(lista):
    """ Este generador toma una lista como parametro y devuelve sus elementos en orden inverso """

    for elemento in lista[::-1]: # Forma pythonica con el mecanismo de slicing
        yield elemento
def generador_inverso_compacto(lista):
    """ Version simplificada y compacta usando expresiones generadoras """

    return (elemento for elemento in lista[::-1]) # Doblemente pythonico: slicing + expresiones generadoras

# Prueba 1 (generador con yield)
mi_lista = [i for i in range(1, 11)] # Otra forma tambien pythonica con list comprehensions

print("Despegue en: ")
for elemento in generador_inverso(mi_lista):
    print(elemento)
print("¡Despegue iniciado!\n")

# Prueba 2 (expresion generadora)
for i in generador_inverso_compacto(mi_lista):
    print(i)
print("Funciona!")