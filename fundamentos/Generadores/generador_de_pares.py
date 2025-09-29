def generar_pares(n):
    for i in range(0, n, 2):
        yield i

numeros_pares = generar_pares(10)

for n in numeros_pares:
    print(n)