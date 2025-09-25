t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x==0 or y==0: print(1)
    
    else:
        f = [[1] * y] * x
        for i in range(1, x):
            for j in range(1, y):
                f[i][j] = f[i-1][j] + f[i][j-1] + f[i-1][j-1]
        print(f[x][y])