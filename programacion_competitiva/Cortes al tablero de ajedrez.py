n = int(input())
piezas = 1
aumento = 1
if n == 0:
    print(piezas)
else:
    for i in range(1, n+1):
        if i%2 == 0:
            aumento += 1
        piezas += aumento
    print(piezas)