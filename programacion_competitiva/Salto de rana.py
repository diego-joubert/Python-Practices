MOD = 1000000007
t = int(input())
r = []
for i in range(t):
    n = int(input())
    formas = [1, 1]
    for j in range(2, n+1):
        formas.append(formas[j-1]+formas[j-2])
    r.append(formas[n])
for i in r:
    print(i%MOD)