m = int(input())
m //= 52
x, k = -1, -1

for i in range(99, 0, -1):
    for j in range(1, i+1):
        if 7*i + 21*j == m:
            x = i
            k = j
            break
print(x)
print(k)