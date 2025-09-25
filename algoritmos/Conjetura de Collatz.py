t = int(input())
r = []
for i in range(t):
    n = int(input())
    secuencia = []
    
    while n!=1:
        secuencia.append(n)
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n +1
    secuencia.append(n)
    r.append(len(secuencia))
for res in r:
    print(res)