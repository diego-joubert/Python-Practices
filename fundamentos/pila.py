class Stack(object):
    def __init__(self):
        self.stack_pointer = None

    def push(self, element):
        self.stack_pointer = Node(element,             self.stack_pointer)
    
    def pop(self):
        e = self.stack_pointer.element
        self.stack_pointer = self.                                stack_pointer.next
        return e

    def peek(self):
        return self.stack_pointer.element

    def __len__(self):
        i = 0
        sp = self.stack_pointer
        while sp:
            i += 1
            sp = sp.next
        return i

class Node(object):
def __init__(self, element=None, next=None):
self.element = element
self.next = next

if __name__ == '__main__':
# small use example
s = Stack()
[s.push(i) for i in xrange(10)]
print [s.pop() for i in xrange(len(s))]