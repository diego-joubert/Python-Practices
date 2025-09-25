import itertools

def subcomandos(s):
    subcomandos = []
    
    for i in range(2, len(s)+1):
        for combinacion in itertools.combinations(s, i):
            subcomandos.append(''.join(combinacion))
    return subcomandos

def ejecutar(s):
    x, y, comandos = 0, 0, 0
    for i in range(len(s)):
        if s[i] == 'U':
            y += 1
        elif s[i] == 'D':
            y -= 1
        elif s[i] == 'L':
            x -= 1
        elif s[i] == 'R':
            x += 1
        if x == 0 and y == 0:
           comandos = i+1
    return comandos
   
n = int(input())
cadena = input()
sc = subcomandos(cadena)
comandos = []

for i in sc:
    comandos.append(ejecutar(i))
print(max(comandos))