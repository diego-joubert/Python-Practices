n = int(input())
asientos = list(input())
pvasos = n+1
pvasos -= asientos.count('L')//2
print(n if pvasos>=n else pvasos)