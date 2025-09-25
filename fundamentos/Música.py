class Instrumento:
    """Abstracción del objeto Instrumento"""
    def __init__(self, precio):
        """Método de inicialización con el atributo precio"""
        self.precio = precio
    
    def tocar(self):
        """Tocar: Método común a todos los objetos de la clase Instrumento"""
        print("Estamos tocando música")
    
    def romper(self):
        print(f"¡Eso lo pagas tú, son {self.precio} dólares!")

class Guitarra(Instrumento):
    """"Subclase de Instrumento"""
    pass

class Bajo(Instrumento):
    pass

mi_guitarra = Guitarra(467.99)
mi_guitarra.romper()