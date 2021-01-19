operators = ['+', '*']

def operate(line):
    result = None
    a, b = None, None
    op = ''
    i = 0
    while i < len(line):
        symbol = line[i]
        print(i, "-->", symbol, "\ta", a, "\tb", b)
        if symbol == ')':
            if a != None:
                print("\treturn) A", a)
                return a
            print("\treturn) R", result)
            return result
        if symbol == '(':
            print("---")
            if a == None:
                a = operate(line[i+1:])
                print("\tA")
            else:
                b = operate(line[i+1:])
                print("\tB")
            print("\ti", i, "\ta", a, "\tb", b)
            j = line[i+1:].index(')')
            if b == None:
                b = operate(line[j+1:])
            print("\t---", a, b)
            result = a + b if op == '+' else a * b
            a = result
            b = None
            i += j + 1
            print("\ti", i, "\ta", a, "\tb", b)
        elif symbol not in operators:
            if a == None:
                a = int(symbol)
            elif b == None:
                b = int(symbol)
                result = a + b if op == '+' else a * b
                a = result
                b = None
        else:
            op = symbol
        i += 1
    print("\treturn", result)
    return result

total = 0

with open("inputEjemplo.txt") as file:
    i = 0
    for line in file:
        # TODO: quitar el split porque no parece tan importante xd?
        symbols = line.rstrip().replace(' ', '')

        print("Linea", i, "--------------------------------------------")
        for h, s in enumerate(symbols):
            a=''
            if h > 9:
                a = ' '
            print(s + a, end=" ")
        print()
        for j, s in enumerate(symbols):
            print(j, end=" ")
        print()
        i += 1

        resultado = operate(list(symbols))
        print("\t", resultado)
        total += resultado
         # -----------------------------------
        #break
    print("Total", total)

# --------------------------------------
print("El ejemplo debe dar", 26457)
