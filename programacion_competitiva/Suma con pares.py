input()
lista = list(map(int, input().split()))
k = int(input())
cont = 0
complementos = set()

for num in lista:
	complemento = k - num
	if complemento in complementos:
		cont += 1
	complementos.add(num)
	
print(cont)
