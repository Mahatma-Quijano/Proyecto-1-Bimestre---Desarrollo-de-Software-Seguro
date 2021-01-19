def operate(line):
    # Si la línea que iteramos tiene mas  de 1 elemento
    while len(line) > 1:
        # Tenemos un ")" como segundo valor de la linea iterada. Ej: ["34",")"]
        if line[1] == ')':
            # En el caso que el ")" sea el último elemento de la línea
            if line[2:] == []:
                return line[0:1]
            # En el caso que despues del ")" tengamos mas elementos. Ej: ["34",")", "+" ...]
            else:
                return line[0:1] + line[2:]
        # Si el primer elemento es un "(", volvemos a operar pero quitando este elemento
        # de la lista que vamos a mandar. Ej : ["(","5","+" ...]
        if line[0] == '(':
            line = operate(line[1:])
        # Si el tercer elemento es un "(", mandamos a operar de nuevo operator
        # tomando en cuenta a partir del cuarto elemento, pero guardando los dos
        #primeras. Ej : ["5", "+", "(", "5" ....]
        elif line[2] == '(':
            line = [line[0], line[1]] + operate(line[3:])
        # Si el segundo elemento es un simbolo "+" o "*", obtengo el primer valor
        # el segundo y el operador, para realizar la operación correspondiente
        # Ej: ["2", "+", "4"]
        elif line[1] == '+' or line[1] == '*': # 0 + 1
            op = line[1]
            a = int(line[0])
            b = int(line[2])
            result = a + b if op == '+' else a * b
            # Generó una nueva lista con el valor calculado y lo demás elementos
            # que todavía estan en la lista
            line = [result] + line[3:]
    return line

total = 0
with open("inputEjemplo.txt") as file:
    # Abrir el archivo y leo por líneas
    for line in file:
        expression = []
        # Crear una lista con los números y símbolos de la línea (quitando los espacios)
        for symbol in line.rstrip().replace(' ', ''):
            if symbol.isnumeric():
                expression.append(int(symbol))
            else:
                expression.append(symbol)
        # Mando a operar la línea
        result = operate(expression)[0]
        # Acomular el resultado de cada línea del archivo
        total += result
    print("Total",total)
print("El ejemplo debe dar", 26457)
