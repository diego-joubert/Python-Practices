n, k = map(int, input().split())
sillas = list(map(int, input().split()))
posiciones = [i for i in range(n) if sillas[i] == k]

if sillas.count(k) < 2:
    print(-1)

d = float('inf')

for i in range(1, len(posiciones)):
    distancia = posiciones[i] - posiciones[i-1]
    d = min(d, distancia)

print(d-1)