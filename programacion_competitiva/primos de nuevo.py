def es_primo(n):
    if n == 0:
        return False
    elif n == 1 or n == 2:
        return True
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True
        
m = int(input())
r1 = []
r2 = []
for i in range(m):
    n = int(input())
    if es_primo(n):
        r1.append(n)
        r2.append(n)
    else:
        for i in range(n, 1, -1):
            if es_primo(i):
                p1 = i
                break
        for j in range(n, n**2):
            if es_primo(j):
                p2 = j
                break
        r1.append(p1)
        r2.append(p2)
for p1, p2 in zip(r1, r2):
    print(f"{p1} {p2}")