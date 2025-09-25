def numPozos(grid):
	if not grid: return 0
	
	fils, cols, len(grid), len(grid[0])
	cont = 0
	
	def dfs(i, j):
		if i < 0 or i >= fils or j < 0 or j >= cols or grid[i][j] == '.':
			return
			
		grid[i][j] = '.'
		
		dfs(i+1, j)
		dfs(i-1, j)
		dfs(i, j-1)
		dfs(i, j+1)
		dfs(i+1, j+1)
		dfs(i-1, j-1)
		dfs(i-1, j+1)
		dfs(i+1, j-1)
		
	for i in range(fils):
		for j in range(cols):
			if grid[i][j] == 'W':
				cont += 1
				dfs(i, j)
	return cont
	

fils, cols = map(int, input().split())
grid = []

for _ in range(fils):
	fil = list(input().strip())
	grid.append(fil)
	
print(numPozos(grid))