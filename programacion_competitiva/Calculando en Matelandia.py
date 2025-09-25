def suma(n):
    return n*(n-1)
t = int(input())
r = []
for i in range(t):
    n = int(input())
    r.append(suma(n))
for _ in r:
    print(_)