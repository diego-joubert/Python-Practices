def generar_divisores(numero):
    """ Funcion generadora que devuelve todos los divisores de un numero desde 1 hasta n """

    for i in range(1, numero+1):
        if numero%i == 0: # Comprobamos si i es divisor de numero y en caso de que lo sea lo devolvemos
            yield i 

# Prueba
n = 12

print(f"Los divisores del numero {n} son: ")

for divisor in generar_divisores(n):
    print(divisor)