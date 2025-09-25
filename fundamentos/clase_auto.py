class Auto:
    
    def __init__(self, marca, modelo, gasolina):
        self.marca = marca
        self.modelo = modelo
        self.gasolina = gasolina
        self.enmarcha = False
    
    def describir(self):
        print(f"Este es un {self.marca} {self.modelo}!")
    
    def arrancar(self):
        if self.gasolina > 0:
            print(f"¡El auto ha arrancado! Tenemos {self.gasolina} litros de combustible.")
            self.enmarcha = True
        else:
            print("No hay gasolina :v")
            self.enmarcha = False
    
    def conducir(self):
        if (self.gasolina > 0) and (self.enmarcha):
            self.gasolina -= 1
            print(f"Quedan {self.gasolina} litros.")
        elif (self.enmarcha == False):
            print("No arrancaste el coche xd")
        else:
            print("No hay gasolina :v")
    
    def chocar(self):
        self.gasolina = 0
        print("¡Se rompió el tanque!")
        print(f"Ahora  quedan {self.gasolina} litros :v")


marca = input("¿De que marca es tu auto?: ")
modelo = input("¿Que modelo es?: ")
gasolina = int(input("¿Cuanta gasolina tiene?: "))
mi_auto = Auto(marca,modelo, gasolina)

while True:
    print("So, ¿que quieres hacer?:")
    e1 = "Describir"
    e2 = "Arrancar"
    e3 = "Conducir"
    e4 = "Chocar"
    e5 = "Salir"
    e6 = "Llenar el tanque"
    print(e1, e2, e3, e4, e6, e5)
    e = input()

    if e == e1:
        mi_auto.describir()
    elif e == e2:
        mi_auto.arrancar()
    elif e == e3:
        mi_auto.conducir()
    elif e == e4:
        mi_auto.chocar()
    elif e == e6:
        cant = int(input("¿Cuanta gasolina le quieres echar?"))
        mi_auto.gasolina += cant
    else:
         break
         