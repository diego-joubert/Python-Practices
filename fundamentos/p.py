t = int(input())
r = []
for i in range(t):
    n = input()
    for j in range(int(n), 10**6):
        if str(j) == str(j[::-1]):
            np = j
    r.append(np)
for i in r:
    print(i)