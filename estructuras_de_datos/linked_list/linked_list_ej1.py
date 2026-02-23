""" Ejercicio numero 1 de la serie de Linked Lists.

Objetivo: Implementar una Singly Lined List con los siguientes metodos:

    - agregar_al_final
    - agregar_al_inicio
    - eliminar_por_valor
    - buscar
    - obtener_tamano
    - imprimir
    - invertir
"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self):
        return str(self.valor)

class SinglyLinkedList:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0


    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            yield nodo_actual
            nodo_actual = nodo_actual.siguiente

    def agregar_al_final(self, data):
        nodo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nodo
        
        else:
            for nodo_actual in self:
                pass
            nodo_actual.siguiente = nodo
            self.tamano += 1

    def agregar_al_inicio(self, data):
        nodo = Nodo(data)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        self.tamano += 1

    def eliminar_por_valor(self, target_node_data):
        if self.cabeza is None:
            print("No es posible eliminar. La lista esta vacia.")
            return

        nodo_anterior = None
        nodo_actual = self.cabeza

        while nodo_actual is not None or nodo_actual.valor != target_node_data:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if nodo_actual is None:
            print(f"El nodo con valor {target_node_data} no ha sido encontrado.")
            return

        nodo_anterior = nodo_actual.siguiente
        nodo_actual = None
        self.tamano -= 1

    def buscar(self, target_node_data):
        if self.cabeza is None:
            return False

        nodo_actual = self.cabeza
        while nodo_actual is not None or nodo_actual.valor != target_node_data:
            nodo_actual = nodo_actual.siguiente
        
        return False if nodo_actual is None else True

    def obtener_tamano(self):
        return self.tamano

    def imprimir(self):
        if self.cabeza is None:
            return

        nodos = []

        for nodo_actual in self:
            nodos.append(str(nodo_actual.valor))
            nodo_actual = nodo_actual.siguiente
        
        print(" -> ".join(nodos))

    def invertir(self):
        if self.cabeza is None:
            return

        nodos = []

        for nodo_actual in self:
            nodos.append(nodo_actual)
            nodo_actual = nodo_actual.siguiente

        nodos.reverse()
        self.cabeza = nodos[0]

        for i in range(self.tamano-1):
            nodos[i].siguiente = nodos[i+1]
        
        nodos[-1].siguiente = None

        

# Pruebas

llist = SinglyLinkedList()
llist.agregar_al_final(10)
llist.agregar_al_final(20)
llist.agregar_al_final(30)
llist.agregar_al_inicio(5)
llist.imprimir()
