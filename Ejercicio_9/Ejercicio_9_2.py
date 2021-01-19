# Variable global que facilita cambiar el preámbulo dado por el ejercicio
# en el inputEjemplo se maneja con 5 y en los demás 25
preamble = 25
# Función que permite encontrar el númeroX (valor corrupto) que no tiene dos valores
# en el preámbulo que sumados entre sí den el númeroX
def attackXMAS (numbers):
    # Varible iterativa que permite moverse en 1 espacio en el array de números
    posVar = preamble
    while True:
        count = 0
        # Se itera dentro de la lista de los 25 números de preambulo al 26vo (valor corrupto)
        # Ej: ["0","1","2",..."24"] para el valor "25" (valor corrupto)
        # Ej: ["1","2",....,"25"] para el valor "26" (valor corrupto)
        for num1 in numbers[posVar - preamble : posVar]:
            # Resto el número del preámbulo (hasta 25 veces)
            buscar = numbers[posVar] - num1
            # Busco dentro de la lista del preámbulo el segundo valor
            if buscar in numbers[posVar - preamble: posVar]:
                # Si esta, set en 0 al conteador y paso al siguiente lista de
                # preámbulo y el posible valor corrupto
                posVar+=1
                count = 0
            else:
                # Subo el contador de fallidos
                count += 1
            # Si el contador llega a 25 (número del preámbulo), se encontró el
            # valor corrupto que no cumple con la propiedad
            if count == preamble:
                return numbers[posVar]

# Función que permite encontrar la lista de valores que su suma produce el valor
# corrupto. Retornando únicamente el mínimo y el máximo de esa lista
def encryptionWeakness (value, numbers):
    actual, base, suma = 0, 0 ,0
    listTemp = []
    while True:
        # Si la suma es menor al valor corrupto, sigo agregando el siguiente número
        # y sobreescribo la suma
        if suma < value:
            listTemp.append(numbers[actual])
            actual +=1
            suma = sum(listTemp)
        # Si el igual, devuelvo el mínimo y máximo de la lista que generó el
        # valor corrupto
        elif suma == value:
            return min(listTemp), max(listTemp)
        # Si la suma es mayor al valor corrupto, set a todo a 0 y el valor base
        # incrementa en 1 (indicar el nuevo inicio para empezar a sumar)
        elif suma > value:
            base += 1
            actual, suma , listTemp = base , 0, []

numbers = []
# Abrir el archivo y almacenar cada número en una lista como enteros
with open("inputDiana.txt") as file:
    for number in file:
        numbers.append(int(number))
# Llamar al método de ataque al algoritmo criptografico "eXchange-Masking Addition System (XMAS)"
value = attackXMAS(numbers)
# Obtener los números mínimo y maximo que general al valor corrupto y se lo suma
min , max  = encryptionWeakness(value,numbers)
print("Máximo:", max, "Mínimo:", min, "Suma:", max+min)
