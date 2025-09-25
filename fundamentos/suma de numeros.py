# Solicitar al usuario que ingrese dos números separados por espacios
entrada = input("Ingrese dos números separados por espacios: ")

# Dividir la entrada en dos partes y convertirlas a números
numero1, numero2 = map(float, entrada.split())

# Calcular la suma
suma = numero1 + numero2

# Mostrar el resultado
print("La suma de {} y {} es: {}".format(numero1, numero2, suma))