def calcular(n, k):
    longitud = len(n)
    suma = sum(list(map(int, n)))
    
    for _ in range(k-1):
        longitud += (longitud-1) * len(n)
        suma += suma * (longitud-1)
    
    return (longitud, suma)
    
v, k, n = map(int, input().split())
res = calcular(str(n), k)

if v==1: print(res[0])
else: print(res[0], "\n", res[1])