from linked_list_ej1 import SinglyLinkedList

def build(valores):
    """ Construye una lista enlazada a partir de los valores dados """

    lista = SinglyLinkedList()

    for valor in valores:
        lista.agregar_al_final(valor)

    return lista

def encontrar_nodo(lista, posicion):
    """ 
    Busca y devuelve el nodo en la posicion indicada. 
    Se garantiza que el parametro posicion siempre es valido.
    """

    if posicion == lista.tamano-1: # Acceso rapido si se busca el ultimo nodo
        return lista.cola


    posicion_actual = 0
    nodo_actual = lista.cabeza

    while nodo_actual:
        if posicion_actual == posicion:
            return nodo_actual
        nodo_actual = nodo_actual.siguiente
        posicion_actual += 1

def crear_lista_con_ciclo(valores, posicion_ciclo):
    """
    Crea una lista enlazada con un ciclo que comienza en posicion_ciclo
    Ej: valores=[1,2,3,4,5], posicion_ciclo=2 crea ciclo en nodo 3
    """
    
    if posicion_ciclo < 0 or posicion_ciclo >= len(valores): # Validar posicion 0-based
        print("Posicion invalida para el ciclo.")
        return


    lista = build(valores)
    nodo_ciclo = encontrar_nodo(lista, posicion_ciclo)

    nodo_actual = lista.cabeza
    while nodo_actual:
        if nodo_actual.siguiente is None:
            break
        nodo_actual = nodo_actual.siguiente
    nodo_actual.siguiente = nodo_ciclo

    return lista

# Prueba de lista con ciclo
arr = [1, 2, 3, 4, 5]
# resultado = crear_lista_con_ciclo(arr, 2)
# resultado.imprimir()
