MOD = 10**9 + 7

def fibo(x, y, memo):
    if (x, y) in memo: return memo[(x, y)]
    
    if x==0 and y==0: resultado=1
    elif x==0:
        resultado= fibo(0, y-1, memo)
    elif y==0:
        resultado = fibo(x-1, 0, memo)
    else:
        resultado = (fibo(x-1, y, memo)) + (fibo(x, y-1, memo)) + fibo(x-1, y-1, memo)%MOD
    
    memo[(x, y)] = resultado
    return resultado
    
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    memo = {}
    
    print(fibo(x, y, memo))
    