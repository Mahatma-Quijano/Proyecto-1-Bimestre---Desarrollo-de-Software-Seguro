def differentOperate(line):
    # Buscar una lista, donde no tenga paréntesis de por medio. Ej :
    # ["(", "5", "+","6","*","2",")"] -> ["5", "+","6","*","2"]
    while '(' in line:
        countParentheticals = 1
        first = line.index('(')
        last = first
        # Buscar el paréntesis correspondiente al que encontremos primero a
        # la izquierda
        while countParentheticals:
            last += 1
            # Si se encuentra otro () dentro de la linea, se suma al countParentheticals
            # para que no se salga hasta que encuentre su par correcto (se haga 0)
            if line[last] == '(':
                countParentheticals += 1
            elif line[last] == ')':
                countParentheticals -=1
        # Una vez encontrada la lista de elementos dentro de los paréntesis
        # Se vuelve a comprobar si no existe otro par de paréntesis interno
        newValue = differentOperate(line[first+1:last])
        # Una vez con elementos númericos y signos, añadimos a la línea esa
        # expresión
        line = line[:first] + newValue + line[last+1:]

    # Con la expresion sin paréntesis, realizamos todas las sumas que se encuentren
    while '+' in line:
        # Guardo la posición del primer "+"
        addPosition = line.index('+')
        # Sumo los valores adyacentes a ese "+"
        a = line[addPosition-1]
        b =line[addPosition+1]
        newValue = a + b
        # Le indico a la linea que se añada el valor sacado (quitando los elementos
        # usados para el cálculo)
        line = line[:addPosition-1] + [newValue] + line[addPosition+2:]

    # Con la expresión sin paréntesis y "+", realizar las multiplicaciones que encuentre
    while '*' in line:
        # Guardo la posición del primer "*"
        multPosition = line.index('*')
        # Multiplico los valores adyacentes a ese "*"
        a = line[multPosition-1]
        b = line[multPosition+1]
        newValue = a * b
        # Le indico a la línea que añada el valor sacado (quitando los elementos
        # usados para el cálculo)
        line = line[:multPosition-1] + [newValue] + line[multPosition+2:]
    return line

total = 0
with open("inputEjemplo.txt") as file:
    # Por cada línea del archivo
    for line in file:
        expression = []
        # Los separo en una lista, donde se elimina los espacios en blanco
        for symbol in line.rstrip().replace(' ', ''):
            if symbol.isnumeric():
                expression.append(int(symbol))
            else:
                expression.append(symbol)
        # Calculo el valor por fila y añado a una variable total
        result = differentOperate(expression)[0]
        total += result
print("resultado", total)

print("deberia dar: 694173")
