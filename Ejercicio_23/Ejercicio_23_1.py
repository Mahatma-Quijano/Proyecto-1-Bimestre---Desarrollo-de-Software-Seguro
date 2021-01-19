from LinkedList import *    # Se importan las clases Node y LinkedList

# Entradas provistas por la página Advent of Code
inputEjemplo = "389125467"
inputMahatma = "952438716"
inputDiana = "327465189"

# Entrada que va a usar
input = inputMahatma

# Se crea una Lista Enlazada para las copas
cups = LinkedList()

# Se añaden las etiquetas de las copas
for num in input:
    cups.add(int(num))

# La Lista Enlazada se hace circular
cups.makeCycle()

# Se obtiene una lista de las copas
array = cups.array()

# Nodo que servirá de apuntador
label = Node(0)
label.setNext(cups.head)

# Bucle por los 100 movimientos del cangrejo
for i in range(100):
    label = label.next # Se actualiza el apuntador
    # Lista de las copas que se levantan (3 siguientes)
    pickedUp = [label.next, label.next.next, label.next.next.next]
    found = False   # Indica si ya se terminó el movimiento
    destination = label.data - 1    # Etiqueta de la copa destino
    while not found:
        # Lista de todas las copas sobre las que se puede iterar
        others = [j for j in array if (j not in pickedUp) and (j != label)]
        # Valor máximo de etiqueta de las copas de la lista others
        mayor = max([j.data for j in others])
        if destination == 0:    # Si se llega a 0, se reemplaza con el máximo
            destination = mayor
        for n in others:    # Se busca la copa de destino
            if n.data == destination:
                # Se colocan las copas levantadas luego del destino y se
                # reorganiza la Lista Enlazada
                label.next = pickedUp[2].next
                right = n.next
                n.next = pickedUp[0]
                pickedUp[2].next = right
                found = True    # Se finaliza el movimiento
                array = cups.array()    # Se actualiza el arreglo
                break
        destination -= 1    # Se actualiza la etiqueta de copa destino

# Se imprimen las copas después de la copa 1
cups.printSince(Node(1))
