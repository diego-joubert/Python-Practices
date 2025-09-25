def Insercion(numeros):
    for i in range(len(numeros)):
        indice = numeros[i]
        a = i - 1
        while a >= 0 and numeros[a] > indice:
            numeros[a+1] = numeros[a]
            a -= 1
        numeros[a+1] = indice
    return numeros
l = [3, 4, 2, 1, 5]
print(Insercion(l))