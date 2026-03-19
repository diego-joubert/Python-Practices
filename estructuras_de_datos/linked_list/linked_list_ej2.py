""" Ejercicio numero 2 de la serie de Linked Lists.

Objetivo: Implementar una Doubly Linked List con los siguientes metodos:

    - agregar_al_final
    - agregar_al_inicio
    - eliminar_por_valor
    - eliminar_desde_final
    - es_palindromo
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class DoublyLinkedList:
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
            self.tamano += 1
            return
        
        self.cola.siguiente = nodo
        nodo.anterior = self.cola
        self.cola = nodo
        self.tamano += 1

    def agregar_al_inicio(self, data):
        """Agrega un nodo con valor data al inicio de la lista

        Args:
            data (any): Valor del nodo que sera anadido.
        """

        nodo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = nodo
            self.tamano += 1
            return

        self.cabeza.anterior = nodo
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        self.tamano += 1

    def eliminar_por_valor(self, target_node_data):
        """Elimina el primer nodo de izquierda a derecha cuyo valor coincida con el buscado.

        Args:
            target_node_data (any): Valor del nodo a eliminar.
        """

        if self.cabeza is None:
            print("Lista vacia. No es posible eliminar.")
            return
        
        encontrado = False

        if target_node_data == self.cabeza.valor:
             encontrado = True
             self.cabeza = self.cabeza.siguiente
             if self.tamano > 1:
                self.cabeza.anterior = None
                
        elif target_node_data == self.cola.valor:
            encontrado = True
            self.cola = self.cola.anterior
            if self.tamano > 1:
                self.cola.siguiente = None
                
        else:
            for nodo_actual in self:
                if nodo_actual.valor == target_node_data:
                    encontrado = True
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                    break

        if not encontrado:
            print(f"El nodo con valor {target_node_data} no ha sido encontrado.")
            return
        
        self.tamano -= 1

    def eliminar_desde_final(self, posicion):
        """Dada una posicion, elimina el nodo en esa posicion contando desde el final. 

        Args:
            posicion (int): Posicion o indice del nodo a eliminar.
        """

        if self.cabeza is None:
            print("Lista vacia. No es posible eliminar.")
            return

        if posicion < 1 or posicion > self.tamano:
            print("Posicion invalida.")
            return
        
        if posicion == 1 and self.tamano == 1:
            self.cabeza = None
            self.cola = None

        elif posicion == 1:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

        elif posicion == self.tamano:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

        else:
            posicion_actual = 1
            nodo_actual = self.cola

            while nodo_actual.anterior is not None:
                if posicion_actual == posicion:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                    break

                posicion_actual += 1
                nodo_actual = nodo_actual.anterior

        self.tamano -= 1

    def es_palindromo(self):
        """Comprueba si la lista es palindroma, es decir, si es la misma lista que su inverso.

        Returns:
            bool: Devuelve True si es palindroma y False de lo contrario.
        """
        if self.cabeza is None:
            print("La lista esta vacia.")
            return
        
        puntero_izquierdo = self.cabeza
        puntero_derecho = self.cola

        while puntero_izquierdo != puntero_derecho:
            if puntero_izquierdo.valor != puntero_derecho.valor:
                return False

            puntero_izquierdo = puntero_izquierdo.siguiente
            puntero_derecho  = puntero_derecho.anterior

        return True

    def imprimir(self):
        """ Imprime los valores de los nodos de la lista en formato legible. """

        if self.cabeza is None:
            return

        nodos = []

        for nodo_actual in self:
            nodos.append(str(nodo_actual.valor))
            nodo_actual = nodo_actual.siguiente
        
        print(" -> ".join(nodos))

llist = DoublyLinkedList()
llist.agregar_al_final(10)
llist.agregar_al_final(20)
llist.agregar_al_final(30)
llist.agregar_al_inicio(5)
llist.imprimir()
llist.eliminar_por_valor(20)
llist.imprimir()
llist.eliminar_desde_final(3)
llist.imprimir()
print(llist.es_palindromo())
llist.agregar_al_final(10)
print(llist.es_palindromo())
            