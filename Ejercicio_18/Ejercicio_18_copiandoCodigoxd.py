def operate(line):
    while len(line) > 1:
        if line[1] == ')':
            return line[0:1] + line[2:]
        if line[0] == '(':
            line = operate(line[1:])
        elif line[2] == '(':
            line = line[0:2] + operate(line[3:])
        elif line[1] == '+' or line[1] == '*':
            a = int(line[0])
            op = line[1]
            b = int(line[2])
            ans = a + b if op == '+' else a * b
            line = [ans] + list(line[3:])
    return line

total = 0
with open("inputMahatma.txt") as file:
    for line in file:
        expression = []
        for symbol in line.rstrip().replace(' ', ''):
            if symbol.isnumeric():
                expression.append(int(symbol))
            else:
                expression.append(symbol)
        result = operate(expression)[0]
        total += result
        #break
    print("TOTAL:", total)
