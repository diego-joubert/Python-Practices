class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

def reverse_k_group(head, k):
    """
    Invierte los nodos de la lista en grupos de k elementos.
    Si el número de nodos no es múltiplo de k, los últimos permanecen igual.

    Ejemplo:
    Lista: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
    k = 3
    Resultado: 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7 -> None
    """
    
    def reverse_segment(inicio, fin):
        prev, curr = None, inicio
        while curr != fin:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    dummy = Nodo(0)
    dummy.next = head
    prev_group = dummy

    while True:
        kth = prev_group
        for _ in range(k):
            kth = kth.next 

            if not kth:
                return dummy.next
            
        next_group = kth.next
        new_head = reverse_segment(prev_group.next, next_group)

        prev_group.next.next = next_group
        prev_group.next = new_head

        prev_group = prev_group.next
        while prev_group.next != next_group:
            prev_group = prev_group.next


nodos = [Nodo(i) for i in range(1, 8)]
for i in range(6):
    nodos[i].next = nodos[i+1]

head = nodos[0]
resultado = reverse_k_group(head, 3)

# Imprimir resultado
while resultado:
    print(resultado.valor, end=" -> ")
    resultado = resultado.next

