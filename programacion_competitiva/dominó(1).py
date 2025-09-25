def cant_fichas(n):
    fichas_totales = 1
    for A in range(0, n):
        B = (n-A)+1
        fichas_totales += B
    return fichas_totales

t = int(input())
r = []

for i in range(t):
    n = int(input())
    r.append(cant_fichas(n))
for i in r:
    print(i)