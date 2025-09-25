d = int(input())

for _ in range(d):
    l1, c1, l2, c2 = map(int, input().split())
    dificultad1 = l1 * c1
    dificultad2 = l2 * c2
    
    dificultad_mas_dificil = max(dificultad1, dificultad2)
    
    print(dificultad_mas_dificil)