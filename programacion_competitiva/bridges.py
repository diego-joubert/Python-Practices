from collections import deque, defaultdict

def bfs(inicio, grafo):
	visitados = set()
	cola = deque([inicio])
	visitados.add(inicio)
	
	while cola:
		nodo = cola.popleft()
		
		for vecino in grafo[nodo]:
			if vecino not in visitados:
				visitados.add(vecino)
				cola.append(vecino)
				
	return len(visitados) == len(grafo)
	
n, m = map(int, input().split())
grafo = defaultdict(list)
aristas = []
cont = 0

for _ in range(m):
	i, j = map(int, input().split())
	aristas.append((i, j))
	grafo[i].append(j)
	grafo[j].append(i)
	
for i, j in aristas:
	grafo[i].remove(j)
	grafo[j].remove(i)
	
	if not bfs(i, grafo):
		cont += 1
	
	grafo[i].append(j)
	grafo[j].append(i)
	
print(cont)