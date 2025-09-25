def criba():
    n = int(input("\t\tCriba de Eratóstenes\n\n Ingrese un límite:"))
    primos = [True]* n
    primos[0] = primos[1] = False
    for i in range(2, n):
        if primos[i]:
            for j in range(i+i, n, i):
                primos[j] = False
    for i in range(n): print(f"{i}: {primos[i]}")  

criba()