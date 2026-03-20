from linked_list_ej1 import Nodo, SinglyLinkedList

def merge_sorted_lists(l1, l2):
    """
    Combina dos listas ordenadas en una sola lista ordenada.
    
    Ejemplo:
    l1: 1 -> 3 -> 5 -> None
    l2: 2 -> 4 -> 6 -> None
    Resultado: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    """

    dummy = Nodo(None)
    tail = dummy
    p1 = l1.cabeza
    p2 = l2.cabeza
    contador = 0
    while p1 and p2:
        if p1.valor < p2.valor:
            tail.siguiente = p1
            p1 = p1.siguiente
        else:
            tail.siguiente = p2
            p2 = p2.siguiente
        tail = tail.siguiente
        contador += 1
    if p1:
        tail.siguiente = p1
        while tail.siguiente:
            tail = tail.siguiente
            contador += 1
    if p2:
        tail.siguiente = p2
        while tail.siguiente:
            tail = tail.siguiente
            contador += 1
    resultado = SinglyLinkedList()
    resultado.cabeza = dummy.siguiente
    resultado.cola = tail
    resultado.tamano = contador
    return resultado

# Vamos a probar a ver si funciona
lista1 = SinglyLinkedList()
lista2 = SinglyLinkedList()
lista1.agregar_al_final(1)
lista1.agregar_al_final(3)
lista1.agregar_al_final(5)
lista2.agregar_al_final(2)
lista2.agregar_al_final(4)
lista2.agregar_al_final(6)
lista1.agregar_al_final(7)

lista_final = merge_sorted_lists(lista1, lista2)
lista_final.imprimir()
    