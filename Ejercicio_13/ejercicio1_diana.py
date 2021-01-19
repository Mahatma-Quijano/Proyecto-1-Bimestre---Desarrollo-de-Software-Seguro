idBus = []
primeraMarca = 0
with open ("inputDiana.txt") as archivo:
    primeraLinea = archivo.readline()
    segundaLinea = archivo.readline()
    primeraMarca = int(primeraLinea)
    for autobus in segundaLinea.split(","):
        if autobus != "x":
            idBus.append(int(autobus))

tiempo = []

for id in idBus:
    espera = (int(primeraMarca/id) + 1)*id - primeraMarca
    tiempo.append((espera,id))
tiempo.sort()
print (tiempo)
menorTiempo = tiempo[0][0]
menorId = tiempo[0][1]
valorRespuesta = menorId*menorTiempo
print("El valor es (ID, Tiempo, ValorBuscado): ", menorId, menorTiempo, valorRespuesta)
