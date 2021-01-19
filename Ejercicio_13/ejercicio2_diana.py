idBus = []
with open ("inputDiana.txt") as archivo:
    primeraLinea = archivo.readline()
    segundaLinea = archivo.readline()
    for autobus in segundaLinea.split(","):
        if autobus == "x":
                idBus.append(0)
        else:
            idBus.append(int(autobus))

tiempo = []
longitud = len(idBus)
maxIdBus = max(idBus)
print (longitud, maxIdBus)
i = 0
while(True):
    minValor = (maxIdBus - longitud)
    maxValor = (maxIdBus + longitud)
    for id in idBus:
        espera = (int(primeraMarca/id) + 1)*id - primeraMarca
        tiempo.append((espera,id))



tiempo.sort()
print (tiempo)
menorTiempo = tiempo[0][0]
menorId = tiempo[0][1]
valorRespuesta = menorId*menorTiempo
print("El valor es (ID, Tiempo, ValorBuscado): ", menorId, menorTiempo, valorRespuesta)

for n in range(mayorIndex + 1, length):
    if busIDs[n] != 0:
        t_n = t_max + n - mayorIndex
        if (t_n % busIDs[n]) != 0:
            break
        else:
            if n == length - 1:
                t_0 = t_max - mayorIndex
                print("Se acabo:", t_0)
                solvedDer = True


### asdasdasd
earliestTS = 0
busIDs = []

with open("inputEjemplo.txt") as file:
    line1 = file.readline()
    earliestTS = int(line1)
    line2 = file.readline()
    for id in line2.rstrip().split(','):
        value = 0 if id == 'x' else int(id)
        busIDs.append(value)

length = len(busIDs)
mayor = max(busIDs)
mayorIndex = busIDs.index(mayor)

print(busIDs)
# [67, 7, 50, 61]
# [0,  1,  2,  3]


mult = 1
solvedIz, solvedDer = False, False
t = -1
while not (solvedIz and solvedDer):
    t_max = mult * mayor
    # izquierda
    for n in range(0, mayorIndex):
        if busIDs[n] != 0:
            t_n = t_max + n - mayorIndex
            if (t_n % busIDs[n]) != 0:
                break
            else:
                if n == mayorIndex - 1:
                    t_0 = t_max - mayorIndex
                    print("Se acabo:", t_0)
                    solvedIz = True
    # derecha
    for n in range(mayorIndex + 1, length):
        if busIDs[n] != 0:
            t_n = t_max + n - mayorIndex
            if (t_n % busIDs[n]) != 0:
                break
            else:
                if n == length - 1:
                    t_0 = t_max - mayorIndex
                    print("Se acabo:", t_0)
                    solvedDer = True
    mult += 1

def findStairs(min, max, busIDs, t_max, mayorIndex):
    for n in range(min, max):
        if busIDs[n] != 0:
            t_n = t_max + n - mayorIndex
            if (t_n % busIDs[n]) != 0:
                break
            else:
                if n == max - 1:
                    t_0 = t_max - mayorIndex
                    print("Se acabo:", t_0)
                    return True
    return False


def asdasdasd():
    solved = False
    m_i = 1 # Multiplicador que itera
    lastIDindex = 0 # Indice de busIDs[0]
    while not solved:
        t = busIDs[0] * m_i
        if t == 754018:
            print("t:", t, "\tm_i:", m_i)
        for n in range(1, length):
            if busIDs[n] != 0:
                m_n = ((n-lastIDindex) + (busIDs[lastIDindex] * m_i)) / busIDs[n]
                t_n = busIDs[n] * m_n
                if t == 754018:
                    print("n:", n, "\tLast:", lastIDindex, "t_n:", t_n, "\tm_n:", m_n)
                if (t_n == t + n) and (n == length-1):
                    print("Resuelto:", t)
                    solved = True
                    break
                lastIDindex = n
        if not solved:
            m_i += 1


####dddsa cuando ejecute antes 

earliestTS = 0
busIDs = []

with open("inputEjemplo.txt") as file:
    line1 = file.readline()
    earliestTS = int(line1)
    line2 = file.readline()
    for id in line2.rstrip().split(','):
        value = 0 if id == 'x' else int(id)
        busIDs.append(value)

length = len(busIDs)
mayor = max(busIDs)
mayorIndex = busIDs.index(mayor)

print(busIDs)
# [67, 7, 50, 61]
# [0,  1,  2,  3]

print("Mayor:", mayor, "MayorIndex:", mayorIndex, "Length:", length)

def findStairs(min, max, busIDs, t_max, mayorIndex):
    #if (mayorIndex == 0) or (mayorIndex == len(busIDs) - 1):
    #    return True, t_max
    for n in range(min, max):
        if busIDs[n] != 0:
            t_n = t_max + n - mayorIndex
            if (t_n % busIDs[n]) != 0:
                break
            else:
                if n == max - 1:
                    t_0 = t_max - mayorIndex
                    return True, t_0
    return False, -1

mult = 1
solvedIzq, solvedDer = False, False
tIzq, tDer = -1, -1
while not (solvedIzq and solvedDer):
    t_max = mult * mayor
    # izquierda
    if mayorIndex == 0:
        solvedIzq = True
        tIzq = t_max
    else:
        solvedIzq, tIzq = findStairs(0, mayorIndex, busIDs, t_max, mayorIndex)
    print("Izq", solvedIzq, tIzq)
    # derecha
    solvedDer, tDer = findStairs(mayorIndex + 1, length, busIDs, t_max, mayorIndex)
    print("Der", solvedDer, tDer)
    if solvedIzq and solvedDer and tIzq == tDer:
        print("Solución:", tIzq)
    mult += 1




def asdasdasd():
    solved = False
    m_i = 1 # Multiplicador que itera
    lastIDindex = 0 # Indice de busIDs[0]
    while not solved:
        t = busIDs[0] * m_i
        if t == 754018:
            print("t:", t, "\tm_i:", m_i)
        for n in range(1, length):
            if busIDs[n] != 0:
                m_n = ((n-lastIDindex) + (busIDs[lastIDindex] * m_i)) / busIDs[n]
                t_n = busIDs[n] * m_n
                if t == 754018:
                    print("n:", n, "\tLast:", lastIDindex, "t_n:", t_n, "\tm_n:", m_n)
                if (t_n == t + n) and (n == length-1):
                    print("Resuelto:", t)
                    solved = True
                    break
                lastIDindex = n
        if not solved:
            m_i += 1
