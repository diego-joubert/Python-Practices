import random as r
from bs import *

print("\t Búsqueda de números")
n = int(input("¿Cuantos elementos va a tener el arreglo?: "))
arr = []
for i in range(n):
    arr.append(r.randint(1, 10))
arr.sort()

objetivo = int(input("¿Que numero desea buscar?: "))
resultado = busqueda_binaria(arr, objetivo)
if resultado != -1:
    print(f"Objetivo encontrado en la posicion {resultado}")
else:
    print("Objetivo no encontrado")