n = int(input())
parcelas = []
max_suma = -10**9

for _ in range(n):
	fil = list(map(int, input().split()))
	parcelas.append(fil)
	
prefix = [[0] * (n+1) for _ in range(n+1)]
	
for i in range(1, n+1):
	for j in range(1, n+1):
		prefix[i][j] = parcelas[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
		
for t in range(1, n+1):
	for i in range(0, n-t+1):
		for j in range(0, n-t+1):
			suma = prefix[i+t][j+t] - prefix[i][j+t] - prefix[i+t][j] + prefix[i][j]
			if suma > max_suma:
				max_suma = suma
				
print(max_suma)