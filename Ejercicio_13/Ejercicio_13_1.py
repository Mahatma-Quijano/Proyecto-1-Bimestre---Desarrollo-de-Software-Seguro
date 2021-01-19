# Variables que van a ser usadas mas adelante
earliestTS = 0
busIDs = []

# Se almacenan los datos del timestamp y los IDs
with open("inputMahatma.txt") as file:
    # Se obtiene el timestamp mas cercano
    line1 = file.readline()
    earliestTS = int(line1)
    # Creamos una lista con los busIDs (las X no se guardan)
    line2 = file.readline()
    for id in line2.split(','):
        if (id != "x"):
            busIDs.append(int(id))

# Arreglo que almacenará los datos para cada ID
timestamps = []

# Por cada autobus
for id in busIDs:
    # Calcular la cantudad de minutos que debe esperar
    wait = (earliestTS // id + 1) * id - earliestTS
    # Añadimos a la lista de timestamps los minutos de espera y el id
    timestamps.append((wait, id))
# Ordenamos para así obtener el que se demore menos
timestamps.sort()

# wait * id
print(timestamps[0][0] * timestamps[0][1])
