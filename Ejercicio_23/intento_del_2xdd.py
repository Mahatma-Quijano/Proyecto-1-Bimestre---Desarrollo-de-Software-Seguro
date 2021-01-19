from LinkedList import *

inputEjemplo = "389125467"
inputMahatma = "952438716"
inputDiana = "327465189"

input = inputEjemplo

cups = LinkedList()

nodo_1 = None
for num in input:
    node = cups.add(int(num))
    if node.data == 1:
        nodo_1 = node

max = max([node.data for node in cups.array()])


maxNum = 1000000
print("ASDASD")
for i in range(max + 1, maxNum):
    cups.add(i)
last = cups.add(maxNum)
last.setNext(cups.array()[0])
print("Ya se lleno!!!")

cups.makeCycle()

moves = 10000000

temp = Node(0)
temp.setNext(cups.head)
label = temp
array = cups.array()
mayor = maxNum

for i in range(moves):
    print(i)
    label = label.next
    pickedUp = [label.next, label.next.next, label.next.next.next] # TODO: xd?
    found = False
    destination = label.data - 1
    while not found:
        others = [j for j in array if (j not in pickedUp) and (j != label)]
        if destination == 0:
            if mayor in pickedUp:
                mayor = min([j.data for j in pickedUp]) - 1
                if mayor == label.data:
                    mayor -= 1
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

print(" --------------------------------- FIN ---------------------------------")

print("1.next", nodo_1.next.data)
print("1.next.next", nodo_1.next.next.data)
print("Producto", nodo_1.next.data * nodo_1.next.next.data)
