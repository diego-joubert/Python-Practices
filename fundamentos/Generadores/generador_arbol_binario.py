""" Programa para crear un generador que recorra un arbol binario en orden (izquierda, raiz, derecha) """

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    """ Implementacion de un arbol binario con un metodo para insertar nodos """

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

def recorrer(arbol):
    """ Esta es la funcion generadora que recorre el arbol """

    def _recorrer(nodo):
        if nodo is not None:
            yield from _recorrer(nodo.izquierdo)
            yield nodo.valor
            yield from _recorrer(nodo.derecho)
    return _recorrer(arbol.raiz)

# Prueba
arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(1)
arbol.insertar(9)

for nodo in recorrer(arbol):
    print(nodo, end=' ')