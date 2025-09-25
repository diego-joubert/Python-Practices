#Fuerza bruta: Generar combinaciones de longitud k

def combinaciones(numeros, combinacion, inicio, k):
    
    for i in range(inicio, len(numeros)):
        combinacion.append(numeros[i])
        combinaciones(numeros,  combinacion, i+1, k)
        combinacion.pop()

numeros = [1, 2, 3, 4, 5]
combinacion = []
combinaciones(numeros, combinacion, 0, 3)