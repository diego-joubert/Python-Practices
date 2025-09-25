n = int(input())
vacas = []
max_longitud = 0
p = [0] * (n+1)

for i in range(n):
	vacas.append(int(input()))

for i in range(1, n+1):
	p[i] = (p[i-1] + vacas[i-1]) % 7

primera_oc = {}
ultima_oc = {}

for idc, valor in enumerate(p):
	if valor not in primera_oc:
		primera_oc[valor] = idc
	ultima_oc[valor] =idc
	
for r in primera_oc:
	longitud = ultima_oc[r] - primera_oc[r]
	if longitud > max_longitud:
		max_longitud = longitud
		
print(max_longitud)