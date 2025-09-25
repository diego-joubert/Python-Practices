d = int(input())
tiempo_total = 0
velocidades = []
for i in range(d):
    h, min, dist = map(int, input().split())
    total_min = h*60 + min
    tiempo_total += total_min
    v = (dist*1000) / min
    velocidades.append(v)

dias = tiempo_total // 1440
horas = (tiempo_total % 1440) // 60
minutos = tiempo_total % 60
max_v = 0
i = 0

while i< len(velocidades):
    if velocidades[i] == max(velocidades):
        max_v = i+1
    i += 1
    
print(dias, horas, minutos, max_v)
