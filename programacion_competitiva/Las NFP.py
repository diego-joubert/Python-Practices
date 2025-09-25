n, f, c = map(int, input().split())
r = []

for i in range(n):
    filas = []
    
    for j in range(f):
        filas.append(input())
    m, n = None, None

    for _ in range(f):
        if '#' in filas[_]:
            m = f - _
            break 
    for k in range(f-1, 0, -1):
        if '#' in filas[k]:
            n = f - k
            break 
    if m is not None and n is not None:
        r.append(m - n)

for x in r:
    print(x)