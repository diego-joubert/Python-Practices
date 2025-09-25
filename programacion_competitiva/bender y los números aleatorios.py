n = int(input())
n = str(n**2)

if len(n) == 7:
    n = int(n[1:5])
    print(n)
elif len(n) == 8:
    n = int(n[2:6])
    print(n)