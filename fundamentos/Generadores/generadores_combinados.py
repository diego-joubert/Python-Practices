""" Una caracteristica interesante que tienen los generadores en Python es que
    unopuede crear varios generadores y combinarlos. Este programa
    muestra como hacer eso con algo muy simple, veamos: Crearemos un total de tres
    generadores, el primero devolvera la secuencia 'A, B, C', el segundo devolvera
    'X, Y, Z' y el tercero combinara ambos generadores para devolver 'A, X, B, Y, C, Z'.  """

# Primer generador, este es el encargado de devolver 'A, B, C'
def gen1():
    yield "A"
    yield "B"
    yield "C"

# Segundo generador, este es el encargado de devolver 'X, Y, Z'
def gen2():
    yield "X"
    yield "Y"
    yield "Z"

# Este es el ultimo generador, el cual intercala ambas secuencias para formar 'A, X, B, Y, C, Z'
def generador_combinado():
    secuencia_1 = gen1()
    secuencia_2 = gen2()

    for elemento1, elemento2 in zip(secuencia_1, secuencia_2):
        yield elemento1
        yield elemento2

# Prueba
secuencia_combinada = generador_combinado()

for elemento in secuencia_combinada:
    print(elemento, end=(', ' if elemento != "Z" else ' '))