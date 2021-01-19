# Clase Nodo
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, node):
        self.next = node

# Clase de Lista Enlazada
class LinkedList():
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.last = newNode
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.setNext(newNode)
            self.last = newNode
        return newNode

    def printSince(self, since):
        node = self.head
        while node.data != since.data:
            node = node.next
        while True:
            node = node.next
            if node.data == since.data:
                break
            else:
                print(node.data, end='')

    def array(self):
        array = []
        node = self.head
        while node.next != self.head:
            array.append(node)
            node = node.next
            if node.next == None:
                break
        array.append(node)
        return array

    def makeCycle(self):
        self.last.setNext(self.head)
