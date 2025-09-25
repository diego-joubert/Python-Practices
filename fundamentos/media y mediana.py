def calcular_c(A, B):
    caso1 = 2*B - A
    caso2 = (A+B)//2
    caso3 = 2*A - B
    return min(caso1, caso2, caso3)

r = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    r.append(calcular_c(A, B))
for i in r:
    print(i)