p, q, n = map(int, input().split())
pares = 0
for a in range(1, p+1):
    for b in range(1, q+1):
        c = (a*b)/(a+b)
        if (a*b)%(a+b) and c <= n:
            pares += 1
print(pares)