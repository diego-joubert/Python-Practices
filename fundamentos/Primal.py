def es_primo(n):
    if n == 0 or n == 1: return False
    for i in range(2, n):
        if n%i == 0: return False
    return True

t = int(input())
r = []
for i in range(t):
    n = int(input())
    if es_primo(n): r.append("SI")
    else: r.append("NO")

for res in r: print(res)