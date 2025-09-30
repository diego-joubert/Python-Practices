def fibo():
    """ Generador infinito de la serie de Fibonacci """

    x, y = 0, 1
    while True:
        yield x
        x, y = y, x+y

# Pequeña prueba (se detiene tras mostrar los primeros 10 terminos para evitar un bucle infinito)
serie = fibo()
cont = 0

for termino in serie:
    if cont >= 10: break
    print(termino, end=(', ' if cont<9 else ' '))
    cont += 1
