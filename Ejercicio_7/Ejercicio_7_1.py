import re
archivo = "inputMahatma.txt"
bagRules = {}
validBags = []

# Se abre el archivo
with open(archivo) as file:
    for line in file:
        # Separamos los datos de cada línea del archivo
        color, info = line.split(" bags contain ")
        data = info.rstrip(".\n").split(", ")
        # Se ignoran las bolsas que no almacenan más bolsas
        if data[0] != "no other bags":
            for bags in data:
                number = int(bags[0])
                patt = re.compile("\sbag[s]*")
                bag = patt.sub('', bags[2:])
                if bag[:10] == "shiny gold":
                    validBags.append(color)
                if color not in bagRules:
                    bagRules[color] = [(number, bag)]
                else:
                    bagRules[color].append((number, bag))

# Iteracion por cada bolsa que lleve a un Shiny Gold
for color in validBags:
    # Búsqueda por cada color del diccionario
    for bagColor in bagRules.items():
        # No repite los colores ya vistos
        if bagColor[0] != color:
            # Por cada bolsa dentro del color del diccionario
            for bag in [bagColor[1][i][1] for i in range(len(bagColor[1]))]:
                # Si la bolsa contiene al color iterado y no se ha repetido
                if bag == color and bagColor[0] not in validBags:
                    validBags.append(bagColor[0]) # La lista incrementa para escanear más posibilidades

# El resultado es la longitud de la lista de colores que llevan a una bolsa Shiny Gold
print("Bolsas que llevan a una Shiny Gold", len(validBags))



# TODO: Ver si se hace o no con recursividad
quit()

def countBags(validBags, dictionary):
    for color in validBags:
        count = 0
        for bag in dictionary[color]:
            if bag[0] != color:
                count = 1 + countBags([bag[0]], dictionary)
        return count
    return 0

print(validBags)
print(countBags(validBags, bagRules))
