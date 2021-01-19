#Inicializamos las variables a utilizar mas adelante
card_publicKey, door_publicKey = 0, 0

#Abrimos el archivo y asignamos los valores de las llaves a ls varaibles ya declaradas
with open("inputDiana.txt") as file:
    card_publicKey = int(file.readline().rstrip())
    door_publicKey = int(file.readline().rstrip())

print("CardPK", card_publicKey)
print("DoorPK", door_publicKey)

value = 1
subjectNumber = 7

# Implementamos el bucle que permita encontrar la cantidad de veces que va a
# iterar el bucle buscando la igualdad de valor calculado a la llave pública
# de la puerta
def getLoopSize(subjectNumber, publicKey):
    value = 1
    i = 0
    while value != publicKey:
        value = (value * subjectNumber) % 20201227
        i += 1
    return i

door_loopSize = getLoopSize(subjectNumber, door_publicKey)
print("Card Loop Size", door_loopSize)
# Para obtener la llave privada, se eleva la llave publica para la cantidad de
# veces que itero el bucle y se saca el resto del resultado
print("Encryption key", pow(card_publicKey, door_loopSize, 20201227))
