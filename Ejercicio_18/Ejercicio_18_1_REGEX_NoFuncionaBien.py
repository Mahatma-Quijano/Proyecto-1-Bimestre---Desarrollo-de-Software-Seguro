import re

total = 0

def findParenth(exp):
    return re.findall("\([0-9]+[^()]+\)", exp)

def operate(exp):
    symbols = ['+', '*']
    exp = re.findall("([0-9]+|[+*])", exp)
    if exp[0] not in symbols and exp[-1] not in symbols:
        while len(exp) > 1:
            a = int(exp[0])
            op = exp[1]
            b = int(exp[2])
            ans = a + b if op == '+' else a * b
            exp = [ans] + list(exp[3:])
        return exp[0]
    print("AAAA")
    return exp

def calculate(exp):
    parenth = findParenth(exp)
    while len(parenth) > 0:
        stack = []
        for e in parenth:
            result = operate(e)
            if isinstance(result, list):
                stack.extend(result)
            else:
                stack.append(result)
        for result in stack:
            exp = re.sub("\([0-9]+[^()]+\)", str(result), exp, 1)
        parenth = findParenth(exp)
    return int(operate(exp))

with open("inputMahatma.txt") as file:
    for line in file:
        expression = line.rstrip().replace(' ', '')

        result = calculate(expression)
        total += result

print("TOTAL:", total)
