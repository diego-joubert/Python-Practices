def es_primo(n):
    if n ==0 or n==1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
            break
    return True
def primorial(n):
    primorial = 1
    for i in range(1, n+1):
        if es_primo(i):
            primorial *= i
    return primorial

t = int(input())
r = []
for i in range(t):
    n = int(input())
    r.append(primorial(n))
for result in r:
    print(result)