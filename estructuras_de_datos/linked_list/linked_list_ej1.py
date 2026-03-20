""" Ejercicio numero 1 de la serie de Linked Lists.

Objetivo: Implementar una Singly Linked List con los siguientes metodos:

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
        self.cola = None
        self.tamano = 0


    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            yield nodo_actual
            nodo_actual = nodo_actual.siguiente

    def agregar_al_final(self, data):
        """Agrega un nodo con valor data al final de la lista

        Args:
            data (any): Valor del nodo que sera anadido.
        """

        nodo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = nodo

        else:
            self.cola.siguiente = nodo
            self.cola = nodo

        self.tamano += 1

    def agregar_al_inicio(self, data):
        """Agrega un nodo con valor data al inicio de la lista

        Args:
            data (any): Valor del nodo que sera anadido.
        """

        nodo = Nodo(data)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        self.tamano += 1

    def eliminar_por_valor(self, target_node_data):
        """Elimina el primer nodo de izquierda a derecha cuyo valor coincida con el buscado.

        Args:
            target_node_data (any): Valor del nodo a eliminar.
        """

        if self.cabeza is None:
            print("No es posible eliminar. La lista esta vacia.")
            return
        
        if self.cabeza.valor == target_node_data:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            self.tamano -= 1
            return

        else:
            nodo_anterior = None
            nodo_actual = self.cabeza

            while nodo_actual:
                if nodo_actual.valor == target_node_data:
                    if nodo_anterior:
                        nodo_anterior.siguiente = nodo_actual.siguiente

                        if nodo_actual == self.cola:
                            self.cola = nodo_anterior

                    else:
                        self.cabeza = self.cabeza.siguiente
                        if self.cabeza is None:
                            self.cola = None
                    self.tamano -= 1
                    return
                

                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente

            print(f"El nodo con valor {target_node_data} no ha sido encontrado.")

    def buscar(self, target_node_data):
        """Busca un nodo en la lista por su valor.

        Args:
            target_node_data (any): Valor del nodo buscado.

        Returns:
            bool: Devuelve True si el nodo ha sido encontrado y False de lo contrario.
        """

        if self.cabeza is None:
            print("La lista esta vacia.")
            return

        return any(nodo.valor == target_node_data for nodo in self)

    def obtener_tamano(self):
        return self.tamano

    def imprimir(self):
        """ Imprime los valores de los nodos de la lista en formato legible. """

        if self.cabeza is None:
            print("La lista esta vacia.")
            return

        nodos = []
        for nodo_actual in self:
            nodos.append(str(nodo_actual.valor))
        
        print(" -> ".join(nodos))

    def invertir(self):
        """ Invierte la lista in-place usando punteros a los nodos. """

        if self.cabeza is None:
            print("La lista esta vacia.")
            return
        
        anterior = None
        actual = self.cabeza
        self.cola = actual
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

# Pruebas

llist = SinglyLinkedList()
llist.agregar_al_final(10)
llist.agregar_al_final(20)
llist.agregar_al_final(30)
llist.agregar_al_inicio(5)
llist.invertir()
llist.imprimir()
