n = int(input())
manolo = []
florencio = []
puntos = 0
for i in range(n):
    manolo.append(int(input()))
for _ in range(1, (2*n)+1):
    if _ in manolo:
        continue
    else:
        florencio.append(_)
for i in range(n):
    cg = [f for  f in florencio if f > manolo[i]]
    if len(cg) == 0:
        continue
    ce = min(cg)
    florencio.pop(florencio.index(ce))
    puntos += 1
print(puntos)