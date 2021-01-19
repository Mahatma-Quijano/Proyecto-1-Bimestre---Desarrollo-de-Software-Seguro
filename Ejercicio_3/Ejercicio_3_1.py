# Variable para almacenar la cantidad de árboles encontrados
arboles = 0

with open("inputMahatma.txt") as file:
    desplX = 0  # Desplazamiento en X
    linea1 = file.readline() # La primera linea se salta
    # Obtenemos la longitud de las líneas del archivo
    longitudX = len(linea1.strip())
    for line in file: # Desplazamiento en Y
        # Nos movemos a la derecha 3 espacios
        desplX += 3
        # Si nos salimos de la cantidad de espacios de una línea, regresamos al inicio
        if (desplX >= longitudX):
            desplX -= longitudX
        # Si donde nos movimos existe un árbol, aumentamos el contador
        if (line[desplX] == '#'):
            arboles += 1

print("Arboles encontrados:", arboles)
