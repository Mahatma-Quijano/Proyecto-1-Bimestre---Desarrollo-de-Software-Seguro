# linecache con el metodo getline permite obtener una línea en específico del archivo
import linecache as lc
archivo = "inputMahatma.txt"

# Variables que van a ser usadas
pc = 1
seenPC = []
acc = 0

# Si la instrucción no esta dentro de la lista de instrucciones visitads, se seguira buscando
while (pc not in seenPC):
    # Se añade el número de línea del archivo ha visitar
    seenPC.append(pc)
    # Obtenemos la línea que vamos a visitar
    line = lc.getline(archivo, pc)
    # Separamos la instrucción del valor númerico
    instruction, parameter = line.split(' ')
    value = int(parameter)
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

print ("ACC Total:", acc)
