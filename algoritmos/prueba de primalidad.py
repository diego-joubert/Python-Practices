def es_primo(n):
    l = list(range(n))
    for i in l:
        if l[i] == 0:
           continue
        elif l[i] == 1 or l[i] == 2:
            return True
        elif n%l[i] == 0:
            return False
        return True

n = int(input())
if abs(n) > 10**7:
    print(f"Error de Overflow: {n} es un numero demasiado grande :(")
elif es_primo(n):
    print(f"{n} es primo.")
else:
    print(f"{n} no es primo.")