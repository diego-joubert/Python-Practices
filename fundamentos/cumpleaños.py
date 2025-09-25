cumpleaños = {}

while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre == " ":
        break
        
    if nombre in cumpleaños:
        print(f"El {cumpleaños[nombre]} es el cumpleaños de {nombre}")
    else:
        print("No tengo informacion de cumpleaños para ti :(")
        cumple = input("Cuando es tu cumpleaños?: ")
        cumpleaños[nombre] = cumple
        print("Base de datos de cumpleaños actualizada con exito!")