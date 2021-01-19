archivo = "inputDiana.txt"

suma = 0
# Se abre el archivo
with open(archivo) as file:
    # Proceso para cada grupo
    for line in file:
        yesAnswers = []
        # Los grupos se separan por líneas en blanco
        while (line != '\n') and (len(line) != 0):
            # Bucle por cada persona
            for letter in line.rstrip():
                # Guarda letras no existentes en el array
                if letter not in yesAnswers:
                    yesAnswers.append(letter)
            line = file.readline()
        # Sumamos la cantidad de respuestas positivas
        suma += len(yesAnswers)

print("La suma de las preguntas de todos los grupos:",suma)
