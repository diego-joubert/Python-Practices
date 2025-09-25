#Función Fibo

def fibo(limite):
    """Función para expresar la Serie de         Fibonacci hasta un límite"""
    
    a, b = 0, 1
    while b <= limite:
        print(b, end = ',')
        a, b = b, a + b

print('Serie de Fibonacci:')
limite = int(input('Ingrese un límite numérico:\n'))
fibo(limite)        