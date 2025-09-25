r, d, p = map(int, input().split())
h = 0;

for i in range(1, r, d):
    for j in range(1, r, p):
        if i == j:
            h += 1
print(h)