def generador(n, m, s):
    while n < m:
        n += s
        yield n

l = list(generador(0, 5, 1 ))
print(l)
for i in l:
    print(i)