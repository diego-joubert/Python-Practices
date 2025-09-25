n = int(input())
casas = list(range(1, n+1))

for i in casas:
    s1 = sum(casas[:i])
    s2 = sum(casas[i+1: n])
    if s1 == s2:
        casa = i

print(casa+1)