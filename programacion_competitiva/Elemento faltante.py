conjunto = list(map(int, input().split()))
n = conjunto.pop(0)
for i in range(1, n+1):
    if not i in conjunto:
        elemento_faltante = i
print(elemento_faltante)