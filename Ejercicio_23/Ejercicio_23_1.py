from LinkedList import *

inputEjemplo = "389125467"
inputMahatma = "952438716"
inputDiana = "327465189"

input = inputDiana

cups = LinkedList()

for num in input:
    cups.add(int(num))

cups.makeCycle()

array = cups.array()

temp = Node(0)
temp.setNext(cups.head)
label = temp

for i in range(100):
    label = label.next
    pickedUp = [label.next, label.next.next, label.next.next.next] # TODO: xd?
    found = False
    destination = label.data - 1
    while not found:
        others = [j for j in array if (j not in pickedUp) and (j != label)]
        mayor = max([j.data for j in others])
        if destination == 0:
            destination = mayor
        for n in others:
            if n.data == destination:
                label.next = pickedUp[2].next
                right = n.next
                n.next = pickedUp[0]
                pickedUp[2].next = right
                found = True
                array = cups.array()
                break
        destination -= 1

cups.printSince(Node(1))
