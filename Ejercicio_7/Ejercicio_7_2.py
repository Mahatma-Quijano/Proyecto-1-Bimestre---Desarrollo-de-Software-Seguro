import re
archivo = "inputDiana.txt"
bagRules = {}

# Se abre el archivo
with open(archivo) as file:
    for line in file:
        color, info = line.split(" bags contain ")
        data = info.rstrip(".\n").split(", ")
        # Se ignoran las bolsas que no almacenan más bolsas
        if data[0] != "no other bags":
            # Se guarda el número y el nombre del color en el dictionario
            for bags in data:
                number = int(bags[0])
                patt = re.compile("\sbag[s]*")
                bagColor = patt.sub('', bags[2:])
                # Almacena no repetidos
                if color not in bagRules:
                    bagRules[color] = [(number, bagColor)]
                else:
                    bagRules[color].append((number, bagColor))

# Funcion recursiva para calcular el número de bolsas
def countBags(color, dictionary):
    if color in dictionary:
        value = 0
        for bag in dictionary[color]:
            # Se almacenan el número de bolsas de un color
            # y se multiplica este número por las bolsas ue se encuentren
            # dentro de el nuevo color
            value += bag[0] + bag[0] * countBags(bag[1], dictionary)
        return value
    return 0 # No cuenta bolsas vacias

numberOfBags = countBags("shiny gold", bagRules)

print("El número de bolsas individuales de nuestro Shiny Gold:",numberOfBags)
