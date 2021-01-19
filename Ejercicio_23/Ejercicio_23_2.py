# Entradas provistas por la página Advent of Code
inputEjemplo = "389125467"
inputMahatma = "952438716"
inputDiana = "327465189"

# Lista que contendrá las copas iniciales (9)
input = []
for num in inputDiana: # Se agrega cada copa de la entrada
    input.append(int(num))

n = 1000000         # Número de copas que se utilizan
moves = 10000000    # Número de movimientos

# Arreglo que contiene las n copas --------------------------------
# Se sustituye la Lista Enlazada por una Lista tal que cada índice
# represente a la etiqueta de la copa, y el valor correspondiente a
# ese índice sea la copa (nodo) siguiente en sentido horario
cups = [None] * (n + 1)

maxCup = max(input) # Etiqueta mayor de las copas iniciales

# Se agregan las copas iniciales a la lista de copas
for i in range(len(input) - 1):
    cups[input[i]] = input[i + 1]

# La última copa apunta a la máxima etiqueta + 1
cups[input[-1]] = maxCup + 1

# Se llenan las copas después de la última etiqueta
for i in range(maxCup + 1, n):
    cups[i] = i + 1     # Se colocan en orden ascendente

# La copa de etiqueta n apunta a la primera copa
cups[n] = input[0]

# Variable que servirá de apuntador
label = input[0]

# Bucle por los 100 movimientos del cangrejo
for i in range(moves):
    # Lista de las copas que se levantan (3 siguientes)
    pickedUp = [cups[label]]
    for _ in range(2):
        pickedUp.append(cups[pickedUp[-1]])
    # La copa "label" apunta a la copa que le sigue a la última "levantada"
    cups[label] = cups[pickedUp[-1]]
    destination = label - 1     # Etiqueta de la copa destino
    # Si la copa destino se encuentra entre las "levantadas"
    # o si se siguió restando 1 hasta llegar a 0
    # Si la mayor se encuentra entre las "levantadas", restará 1 desde esa copa
    while destination in pickedUp or destination == 0:
        destination -= 1
        if destination < 1:  # Si se llegó a 0 se elige la mayor
            destination = n
    # Al encontrar la copa destino ---------------------------------------
    #   El apuntador de la última apunta a la siguiente al destino
    cups[pickedUp[-1]] = cups[destination]
    #   La copa de destino apunta a la primera "levantada"
    cups[destination] = pickedUp[0]
    #   La copa "actual" apunta a la siguiente
    label = cups[label]

# Se obtienen las dos copas siguientes a la copa "1"
a = cups[1]
b = cups[a]

# Se imprime el producto de sus etiquetas
print(a * b)
