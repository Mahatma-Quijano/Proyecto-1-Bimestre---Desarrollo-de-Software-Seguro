import math

# Variables que van a ser usadas mas adelante
earliestTS = 0
busIDs = []

with open("inputMahatma.txt") as file:
    # Se obtiene el timestamp mas cercano
    line1 = file.readline()
    earliestTS = int(line1)
    # Creamos una lista con los busIDs (las X se guardan como 0)
    line2 = file.readline()
    for id in line2.rstrip().split(','):
        value = 0 if id == 'x' else int(id)
        busIDs.append(value)

length = len(busIDs) # Cantidad de IDs y X obtenidas

# Funcion que devuelve el Mínimo Común Múltiplo acumulado
def mcm(buses):
    mcm = buses[0]
    for busID in buses[1:]:
        # Por cada id acumula el MCM
        mcm = mcm * busID // math.gcd(mcm, busID)
    return mcm

# Lista que almacena los buses que se encuentran ya ordenados
diagonal = list()
diagonal.append(busIDs[0])

# Timestamp inicial
t = 0
# mcm inicial
mcm_t = mcm(diagonal)
while True:
    t += mcm_t # Se acumula el mcm de los IDs ya ordenados
    for index, id in enumerate(busIDs):
        if id != 0: # Los IDs no son X
            # ¿El bus se encuentra en la posicion deseada?
            # ¿El ID no está aún en la lista de buses ordenados?
            if ((t + index) % id == 0) and (id not in diagonal):
                diagonal.append(id)
                mcm_t = mcm(diagonal) # Se actualiza el mcm de los IDs ordenados
    # ¿Todos los buses han sido ordenados?
    if len(diagonal) + busIDs.count(0) == length:
        break

print("T =", t)
