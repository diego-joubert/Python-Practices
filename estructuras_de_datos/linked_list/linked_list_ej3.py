from linked_list_ej1 import SinglyLinkedList


inf = 10**18

def rellenar(lista, tamano_objetivo):
    for _ in range(tamano_objetivo - lista.obtener_tamano()):
        lista.agregar_al_final(inf)

def merge_sorted_lists(l1, l2):
    """
    Combina dos listas ordenadas en una sola lista ordenada.
    
    Ejemplo:
    l1: 1 -> 3 -> 5 -> None
    l2: 2 -> 4 -> 6 -> None
    Resultado: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    """

    if l1.obtener_tamano() < l2.obtener_tamano():
        rellenar(l1, l2.obtener_tamano())
    else:
        rellenar(l2, l1.obtener_tamano())

    resultado = SinglyLinkedList()

    for nodo1, nodo2 in zip(l1, l2):
        if nodo1.valor < nodo2.valor:
            if nodo1.valor != inf: resultado.agregar_al_final(nodo1)
            if nodo2.valor != inf: resultado.agregar_al_final(nodo2)
        else:
            if nodo2.valor != inf: resultado.agregar_al_final(nodo2)
            if nodo1.valor != inf: resultado.agregar_al_final(nodo1)

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
    