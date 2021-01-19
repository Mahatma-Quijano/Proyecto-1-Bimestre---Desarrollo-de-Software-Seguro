import re

total = 0

def findParenth(exp):
    #regex = "\([^()+*]+\)"
    regex = "[^()]+"
    parenth = re.findall(regex, exp)
    regex2 = "([0-9]+|[+*])"
    print("Regex1", parenth)
    array = [re.findall(regex2, p) for p in parenth]
    print("Regex2", array)
    #return array
    print("Regex3", re.split('([0-9])', exp))
    return array

def operate(exp):
    print("Operate:", exp)
    symbols = ['+', '*']
    #exp = parenth[1:len(parenth)-1]
    if exp[0] not in symbols and exp[-1] not in symbols:
        while len(exp) > 1:
            a = int(exp[0])
            op = exp[1]
            b = int(exp[2])
            ans = a + b if op == '+' else a * b
            exp = [ans] + list(exp[3:])
        #return ['('] + list(exp) + [')']
        return exp[0]
    return exp

def calculate(exp):
    parenth = findParenth(exp)
    #while len(exp) > 1:
    while len(parenth[0]) > 1: # TODO and len(parenth) >= 1:
        print("Exp:", exp)
        stack = []
        for e in parenth:
            result = operate(e)
            if isinstance(result, list):
                stack.extend(result)
                print("\t\tExt", result)
            else:
                stack.append(result)
                print("\t\tApp", result)
        print("Stack:", stack)
        exp = ''.join(map(str, stack))
        print("Changed:", exp)
        parenth = findParenth(exp)
        print("Parenth:", parenth)
    return int(exp)

with open("..\inputEjemplo.txt") as file:
    for line in file:
        expression = line.rstrip().replace(' ', '')

        result = calculate(expression)
        total += result
        print("----------------------------------\tRESULT", result)
        break #----

print("TOTAL:", total)
