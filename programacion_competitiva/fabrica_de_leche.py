n = int(input())
grado_salida = [0] * (n+1)
cont = 0
estacion = 0

for _ in range(n-1):
	a, b = map(int, input().split())
	grado_salida[a] += 1
	
for i in range(1, n+1):
	if grado_salida[i] == 0:
		cont += 1
		estacion = i
		
if cont == 1:
	print(estacion)
else:
	print(-1)