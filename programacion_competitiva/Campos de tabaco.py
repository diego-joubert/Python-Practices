n, m, q = map(int, input().split())
campo = [[0] * m for _ in range(n)]
p = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
	fil = [x for x in list(map(int, input().split())) if x > 0]
		
for i in range(1, n+1):
	for j in range(1, m+1):
		p[i][j] = campo[i-1][j-1] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
		
for _ in range(q):
	x1, y1, x2, y2 = [x-1 for x in list(map(int, input().split()))]
	
	s = p[x2][y2] - p[x1-1][y1-1] - p[x1][y1-1] + p[x1-1][y1-1]
	print(s)