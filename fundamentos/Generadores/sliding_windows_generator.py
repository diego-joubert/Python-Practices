def sliding_windows_generator(lista, k):
    """ Funcion generadora de ventanas deslizantes. Dada una lista y un numero k, el generador devuelve ventanas de tamaño k """

    inicio, fin = 0, k-1
    while fin<len(lista):
        ventana = lista[inicio:fin+1]
        yield ventana

        inicio += 1
        fin += 1

# Prueba
mi_lista = [i for i in range(1, 11)]
ventanas = sliding_windows_generator(mi_lista, 2) # Todas las ventanas de tamaño 2 en una lista con numeros del 1 al 10

for ventana in ventanas:
    print(ventana)