input()
t = sum(list(map(int, input().split())))
m = int(input())
periodos = []
res = -1

for i in range(m):
    l, r = map(int, input().split())
    periodos.append((l, r))

for l, r in periodos:
    if r >= t:
        res = max(l, t)
        break
        
print(res)      