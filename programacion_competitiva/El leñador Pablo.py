def madera(arboles, altura):
    return sum(i-altura for i in arboles if i > altura)
    
n, m = map(int, input().split())
arboles = list(map(int, input().split()))

inicio, fin = 0, max(arboles)

while(inicio < fin):
    medio = (incio + fin+1)//2
    if madera(arboles, medio) >= m:
        incio = medio
    else:
        fin = medio - 1

print(inicio)