def bacterias(n):
    b = 0
    if n==2: return 1
    
    if n%2==0:
        return b + bacterias(n/2)
    else:
        b += 1
        return b + bacterias(n-1)
        
n = int(input())
print(bacterias(n))