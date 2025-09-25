from collections import Counter

n, q = map(int, input().split())
vacas = [0] * (n+1)

for i in range(1, n+1):
	vacas[i] = int(input())
	
for _ in range(q):
	a, b = map(int, input().split())
	frec = Counter(vacas[a:b+1])
	print(frec[1], frec[2], frec[3])	