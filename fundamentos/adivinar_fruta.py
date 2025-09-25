import random
frutas = ["manzana", "piña", "fresa", "melocoton", "banana", "naranja", "uva", "mango"]
fruta_aleatoria = random.choice(frutas)
intentos = 0

while True:
    intentos += 1
    intento = input("Adivina la fruta secreta:")
    
    if intento != fruta_aleatoria:
        print("Fallaste, fruta equivocada. Prueba de nuevo")
    else:
        print(f"Adivinaste, te tomó {intentos} intentos")
        break
   