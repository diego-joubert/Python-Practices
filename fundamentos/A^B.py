def ultimo_digito(a, b):
    if b==0:
        return 1
    ult_digito = a%10
    ciclos = {0: [0], 1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1]}
    
    ciclo = ciclos[ult_digito]
    long_ciclo = len(ciclo)
    
    if b%long_ciclo == 0:
        return ciclo[-1]
    else:
        return ciclo[(b%long_ciclo)-1]
        
t = int(input())
r = []
for _ in range(t):
    a, b = map(int, input().split())
    r.append(ultimo_digito(a, b))
for i in r:
    print(i)