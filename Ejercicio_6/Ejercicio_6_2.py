archivo = "inputDiana.txt"
suma = 0

# Se abre el archivo
with open(archivo) as file:
    # Proceso para cada grupo
    for line in file:
        yesAnswers = {}
        personas = 0
        # Cada persona
        while (line != '\n') and (len(line) != 0):
            personas += 1
            # Crea el diccionario con las preguntas de la primera persona del grupo
            if len(yesAnswers) == 0:
                for letter in line.rstrip():
                    yesAnswers[letter] = 1
            else:
                # Cuenta solo aquellas preguntas que ya se encuentren en la primera persona
                for letter in line.rstrip():
                    if letter in yesAnswers:
                        yesAnswers[letter] = yesAnswers.get(letter, 0) + 1
            line = file.readline()
        # Cuenta aquellas preguntas que hayan sido afirmativas para cada persona
        for letter in yesAnswers:
            if yesAnswers[letter] == personas:
                suma += 1

print("La suma de las preguntas similares por grupo es:",suma)
