t = int(input())

for _ in range(t):
    entrada = input()
    n = int(entrada[0])
    parejas = entrada[2:]
    
    if n%2==0 and parejas.count(">") == parejas.count("<"):
        print("Balanceada")
    else: print("No Balanceada")