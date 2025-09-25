def cuadrante(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

c1 = cuadrante(x1, y1)
c2 = cuadrante(x2, y2)

if c1 == c2:
    print("SI")
else:
    print("NO")