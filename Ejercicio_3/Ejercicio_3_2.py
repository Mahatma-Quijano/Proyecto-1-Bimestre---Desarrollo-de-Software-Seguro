#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.

# Lista con los patrones de movimiento
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
#slopes = [(3, 1)]

desplX = [0] * len(slopes)
arbolesEncontrados = dict()

with open("inputMahatma.txt") as file:
    linea1 = file.readline() # La primera linea se salta
    #print(-1, linea1) # TODO ------------------------------------------------------------------------------------
    longitudX = len(linea1.rstrip())
    for counter, line in enumerate(file): # Desplazamiento en Y
        #print(counter, line) # TODO --------------------------------------------------------------------------------------
        for i, (x, y) in zip(range(len(slopes)), slopes):
            #if (counter % 2 == 0) and (y == 2): #------------------------------------------------------------
            # Nos movemos hacia abajo la cantidad que dice el patrón actual
            if (counter % y == 0) and (y != 1):
                continue
            # Nos desplazamos en X la cantidad de veces que dice el patrón actual
            desplX[i] += x
            # Si nos salimos del máximo de lineas, regresamos al inicio
            if (desplX[i] >= longitudX):
                desplX[i] -= longitudX
            # Si nos topamos con un árbol, incrementamos el contador del patrón actual
            if (line[desplX[i]] == '#'):
                name = f'Slope({x},{y})'
                arbolesEncontrados[name] = arbolesEncontrados.get(name, 0) + 1
# Imprimimos la cantidad de árboles encontrados por patrón
print("Arboles encontrados:")
producto = 1
for a, b in arbolesEncontrados.items():
    print(a + ":", b)
    # Multiplicamos los árboles de cada patrón
    producto *= b

print("Producto:", producto)
