class Node:
    """Definicion del Nodo"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class DoublyNode(Node):
    """Implementacion de un nodo especial para las Doubly Linked Lists"""

    def __init__(self, data):
        super(DoublyNode, self).__init__(data)
        self.prev = None


class LinkedList:
    """Implementacion basica de una Singly Linked List."""

    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        return " -> ".join(map(str, nodes))

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("La lista esta vacia")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Nodo con dato {target_node_data} no encontrado")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("La lista esta vacia")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        for node in self:
            if node.next.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Nodo con dato {target_node_data} no encontrado")

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("La lista esta vacia")

        if self.head.data == target_node_data:
            self.head = self.head.next

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception(f"Nodo con dato {target_node_data} no encontrado")

    def get(self, idc=0):
        if self.head is None:
            raise Exception("La lista esta vacia")

        nodes = []
        for node in self:
            nodes.append(node)

        try:
            return nodes[idc]
        except IndexError:
            print(f"Indice fuera de rango, solo hay {len(nodes)} nodos")
            return

    def reverse(self):
        if self.head is None:
            raise Exception("La lista esta vacia")


class DoublyLinkedList:
    """Implementacion de una Doubly Linked List desde cero"""

    def __init__(self, data=None):
        self.head = None


class Queue(LinkedList):
    """Implementacion de una cola usando linked lists"""

    def __init__(self):
        super(Queue, self).__init__()

    def enqueue(self, data):
        return self.add_last(Node(data))

    def dequeue(self):
        if self.head is None:
            raise Exception("La lista esta vacia")

        node_data = self.head.data
        self.head = self.head.next

        return node_data


llist = LinkedList([1, 2, 3])
print(llist)

# Iterar sobre la linked list
for element in llist:
    print(element)

llist.add_last(Node(4))
print(llist)

llist.add_before(4, Node(3.5))
print(llist)

# Acceso por indice (nueva funcionalidad)
third_node = llist.get(5)
print(third_node)

# Probemos a usar una cola
queue = Queue()
queue.enqueue("Fred")
queue.enqueue("Martha")
queue.enqueue("Susan")

print(queue)

# Atendamos a quien llego primero
first_client = queue.dequeue()
print(first_client)

# ¿Como quedara la cola ahora?
print(queue)
