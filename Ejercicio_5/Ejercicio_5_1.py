# Declarar variables para usar mas adelante
archivo = "inputDiana.txt"
planeRows = 128
planeColumns = 8

# Función que permite calcular el valor del asiento de manera recursiva
def binarySeat(min, max, string):
    # Retorna el valor buscado (después de las 7 o 3 iteraciones)
    if min == max:
        return min
    # Toma la primera letra
    letter = string[0]
    medio = (min + max) // 2
    # Recursividad cambiando los parámetros
    if letter == "F" or letter == "L":
        return binarySeat(min, medio, string[1:])
    elif letter == "B" or letter == "R":
        return binarySeat(medio + 1, max, string[1:])

maxID = 0

# Se abre el archivo
with open(archivo) as file:
    # Cada Boarding Pass (Asiento)
    for seat in file:
        # Obtener las letras para la fila y columna por separado
        rows = seat[:7]
        columns = seat[7:]
        # Calcular el numero de fila y columna del asiento seleccionado
        fila = binarySeat(0, planeRows - 1, rows)
        columna = binarySeat(0, planeColumns - 1, columns)
        # Cálculo ID
        seatID = 8 * fila + columna
        if seatID > maxID:
            maxID = seatID

print("El ID de asiento máximo es:", maxID)
