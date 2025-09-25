n = int(input())
k = int(input())
arr = []
res = 10**9

for _ in range(n):
	arr.append(int(input()))

inicio, fin = 0, k
while inicio<=fin and fin < n:
	res = min(res, fin-inicio)
	inicio += 1
	fin += 1
	
print(res)