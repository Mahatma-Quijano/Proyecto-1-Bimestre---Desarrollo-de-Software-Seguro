archivo = "inputDiana.txt"
# Varaibles a usar mas adelante
pc = 0
acc = 0
seenPC = {}
bootCode = []

# Método que permite la obtención de las tuplas (instruccion:valor) y
# almacenarla en un arreglo bootCode
def getCode(archivo, bootCode):
    with open(archivo) as file:
        for line in file:
            instruction, parameter = line.split(' ')
            value = int(parameter)
            bootCode.append((instruction, value))

# Función que permite iterar si la instrucción no esta dentro de la lista de instrucciones
# visitadas o llego al final del archivo... se seguirá buscando
def runCode(code, pc, seenPC, acc):
    while (pc not in seenPC.keys()) and (pc < len(code)):
        seenPC[pc] = acc
        instruction = code[pc][0]
        value = code[pc][1]
        # ACC: Incrementamos el acc con el valor de la línea visitada y pasamos a la
        # siguiente línea
        if instruction == "acc":
            acc += value
            pc += 1
        # JMP: Sumamos la posición actual con el valor, para saber a que línea dirigirse
        elif instruction == "jmp":
            pc += value
        # NOP: No hace nada especial, solo avanzamos a la siguiente línea
        elif instruction == "nop":
            pc += 1

    if pc in seenPC.keys(): # TODO: Esto solo imprime el valor que encontro repetido
        print(instruction, value) # TODO: Asi que no sirve de nada

    return acc, pc, seenPC

# Obtenemos las tuplas
getCode(archivo, bootCode)
# Llamamos a la función suponiendo que el archivo no esta corrupto
acc, pc, seenPC = runCode(bootCode, pc, seenPC, acc)

# Si el archivo no esta corrompido, obtenemos la respuesta
if pc >= len(bootCode):
    print("ACC Final:", acc)
else:
    #Iteramos por las instrucciones vistas
    for i in set(seenPC.keys()):
        # Tomamos el nombre la instrucción
        instruction = bootCode[i][0]
        flag = False
        nextPC = i # TODO: no es necesario ponerle i
        # Si la instrucción es JMP, le damos el comportamiento del NOP
        if instruction == "jmp":
            nextPC = i + 1
            # Si el siguiente JMP no esta en la lista de los visitados
            # la bandera se hace true, para que vuelva a iterar
            if nextPC not in seenPC.keys():
                flag = True
        # Si la instrucciónes NOP, le damos el comportamiento del JMP
        if instruction == "nop":
            value = bootCode[i][1]
            nextPC = i + value
            # Si el siguiente no esta en la lista de los visitados
            # la badnera se hace truem para que vuelva a iterar
            if nextPC not in seenPC.keys():
                flag = True
        # Si es True, vuelvo a iterar con el nuevo pc inicial y la lista
        # de visitados
        if flag:
            acc, pc, _ = runCode(bootCode, nextPC, seenPC, seenPC[i])
        # Se llego a la última línea del archivo de instrucciones
        if pc >= len(bootCode):
            print("ACC Final:", acc)
            break
