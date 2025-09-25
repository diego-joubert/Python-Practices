secuencia = [i for i in range(2, 10**4, 2)]
r = []
q = int(input())
for i in range(q):
    n = int(input())
    r.append(sum(secuencia[:n]))
for j in r:
    print(j)