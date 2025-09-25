class miError(Exception):
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return "Error "+ str(self.valor)



def dividir(a,b):
    d = a/b
    return d

try:
    print(dividir(float(input()), float(input())))
    raise miError(4)
except (ZeroDivisionError, miError, e):
    print("No se puede dividir un numero por cero!")
    print(e)
else:
    print("Todo esta bien")
finally:
    print("Limpiando.........")
    