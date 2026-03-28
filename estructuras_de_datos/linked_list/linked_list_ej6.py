""" 

Ejercicio numero 6 de la serie de linked list.

Objetivo: Implementar un sistema de Cache LRU (Last Recently Used) usando
          listas enlazadas y tablas hash.

"""

class LRUCacheOptimizado:
    """
    Implementa LRU Cache usando:
    - Doubly Linked List para orden de uso
    - Hash Map para acceso rápido O(1)

    Debe tener complejidad O(1) para get y put
    """

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None


    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = {}
        self.cabeza = self.Node(0, 0)
        self.cola = self.Node(0, 0)
        self.cabeza.next = self.cola
        self.cola.prev = self.cabeza
        self.tamano = 0

    def _agregar_nodo(self, nodo):
        """Agrega nodo después de cabeza (más reciente)"""

        nodo.prev = self.cabeza
        prev = self.cabeza.next
        self.cabeza.next = nodo
        nodo.next = prev
        prev.prev = nodo


    def _remover_nodo(self, nodo):
        """Remueve nodo de la lista"""
        
        nodo.prev.next = nodo.next
        nodo.next.prev = nodo.prev

    def _mover_al_frente(self, nodo):
        """Mueve nodo existente al frente"""
        
        self._remover_nodo(nodo)
        self._agregar_nodo(nodo)


    def _eliminar_lru(self):
        """Elimina el nodo antes de cola (menos reciente)"""
        
        nodo = self.cola.prev
        self._remover_nodo(nodo)
        del self.cache[nodo.key]
        self.tamano -= 1

    def get(self, key):

        """Busca y devuelve el nodo que tenga la clave key.

        Returns:
            Nodo: El nodo con la clave solicitada.
        """
        
        if self.tamano == 0:
            print("El cache esta vacio.")
            return -1

        if key not in self.cache:
            print(f"El nodo con la clave {key} no esta en el cache.")
            return -1
        
        nodo = self.cache[key]
        self._mover_al_frente(nodo)
        return nodo.value

    def put(self, key, value):
        """Agrega un nodo al cache.

        Args:
            key (hasheable): Clave del nodo a agregar. Debe ser hasheable (unica e inmutable).
            value (any): Valor del nodo a agregar.
        """
        
        if key in self.cache:
            # Actualizar valor y mover al frente
            nodo = self.cache[key]
            nodo.value = value
            self._mover_al_frente(nodo)
        else:
            # Crear nuevo nodo
            nodo = self.Node(key, value)
            self.cache[key] = nodo
            self._agregar_nodo(nodo)
            self.tamano += 1
            # Si excede capacidad, eliminar LRU
            if self.tamano > self.capacidad:
                self._eliminar_lru()


    def imprimir_estado(self):
        """Muestra el estado actual del cache"""
        print("Cache estado:")
        print(f"Capacidad: {self.capacidad}, Tamaño: {self.tamano}")

        # Mostrar orden de uso (de más reciente a menos)
        actual = self.cabeza.next
        orden = []
        while actual != self.cola:
            orden.append(f"{actual.key}:{actual.value}")
            actual = actual.next
        print(f"Orden: {' -> '.join(orden)}")

        # Mostrar contenido del hash map
        print(f"Hash Map: {list(self.cache.keys())}")

# Prueba detallada
cache = LRUCacheOptimizado(3)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.imprimir_estado()

cache.get(1)  # Debe mover 1 al frente
cache.imprimir_estado()

cache.put(4, "D")  # Debe eliminar 2 (LRU)
cache.imprimir_estado()
