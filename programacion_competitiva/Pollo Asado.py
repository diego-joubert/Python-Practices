n = int(input())
r = []
for i in range(n):
    x = int(input())
    if (x/3 == 0) or (x//7 == 0) or (x%7)%3 == 0:
        r.append("YES")
    else:
        r.append("NO")
for i in r:
    print(i)