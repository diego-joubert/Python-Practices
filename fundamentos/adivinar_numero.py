import random

numero_secreto = 101
intentos = 0

while True:
  intentos += 1
  intento = int(input("Adivina el número (entre 1 y 100): "))

  if intento < numero_secreto:
    print("El número es mayor.")
  elif intento > numero_secreto:
    print("El número es menor.")
  else:
    print(f"¡Adivinaste! Te tomó {intentos} intentos.")
    break