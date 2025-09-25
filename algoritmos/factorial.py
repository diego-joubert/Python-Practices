def factorial(n):
  """
  Esta función calcula el factorial de un número.

  Args:
    n: El número para el cual se calculará el factorial.

  Returns:
    El factorial del número.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def factorialN(n):
    if n==0:
        return 1
    else:
        return n*factorialN(n+1)
   
numero = int(input("Ingresa un número: "))

if numero < 0:
 print(factorialN(numero))
elif numero == 0:
  print("El factorial de 0 es 1.")
else:
  resultado = factorial(numero)
  print(f"El factorial de {numero} es {resultado}.")