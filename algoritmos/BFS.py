from collections import deque

def BFS(inicio, grafo):
    visitados = [False] * len(grafo)
    cola = deque([inicio])
    
    visitados[inicio] = True
    
    while cola:
        nodo = cola.popleft()
        print(nodo, end = " ") #Procesar 
        
        for vecino in grafo[nodo]:
            if not visitados[vecino]:
                visitados[vecino] = True
                cola.append(vecino)
                
grafo = [[1, 4], [0, 4, 3, 2], [1, 3], [2, 1, 4], [0, 1, 3]]

for i in range(len(grafo)):
    print(f"BFS iniciando desde el nodo {i}:", end = " ")
    BFS(i, grafo)
    print("\n")