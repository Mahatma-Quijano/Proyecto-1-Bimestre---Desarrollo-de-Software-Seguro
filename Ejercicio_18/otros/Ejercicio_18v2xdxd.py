def asdasdasd(line):
    result = 0
    op = ''
    for i, symbol in enumerate(line):
        if symbol == ')':
            return result
        #if symbol == '+' or symbol == '*':
        #    op = symbol
        if symbol != '(' and not (symbol == '+' or symbol == '*'):
            a = int(symbol)
            if line[i+1] == '+':
                return a + operate(line[1:])
            elif line[i+1] == '*':
                return a * operate(line[1:])
        else: # (
            pass
    return result



operators = ['+', '*']

def operate1(line):
    result = 0
    for i, symbol in enumerate(line):
        if symbol == '(':
            return operate1(line[1:])
        elif symbol == ')':
            if i+1 < len(line):
                if line[i+1] == '+' or line[i+1] == '*':
                    op = line[i+1]
                    b = operate1(line[i+2:])
                    result = result + b if op == '+' else result * b
            return result
        elif symbol not in operators:
            if i+1 < len(line):
                op = line[i+1]
                a = int(symbol)
                b = operate1(line[i+1:])
                print("\t", a, "-->", b)
                return a + b if op == '+' else a * b
            return int(symbol)
    return result

#def operate2(prev = None, line):
#    ans = None
#    if line[0].isnumeric():
#        ans = int(line[0])
#        if len(line) > 0:
#            return operate(line[0], line[1:])
#    elif line[0] == '+' or line[0] == '*':
#        if line[1].isnumeric():
#            ans = prev + line[1] if line[0] == '+' else prev * line[1]
#        else:
#            pass
#    elif line[0] == ')':
#        return ans

def operate3(line):
    print(line)
    ans = 0
    if len(line) == 1:
        print("\treturn1", int(line[0]))
        return int(line[0])
    else:
        if line[0].isnumeric():
            if line[1] == '+' or line[1] == '*':
                a = int(line[0])
                b = operate(line[2:])
                ans = a + b if line[1] == '+' else a * b
                print("a", a, "\tb", b, "\tans", ans)
            else: # )
                if len(line[1:]) > 1:
                    b = operate(line[2:])
                    ans = ans + b if line[1] == '+' else ans * b
                    print("a", ans, "\tb", b, "\tans", ans)
                    #return ans
                else:
                    print("\treturn2", int(line[0]))
                    return int(line[0])
        else: # (
            asd = operate(line[1:])
            print("\tReturn (", asd)
            return asd
    return ans

def eval_expr(ex):
    # a is always a literal
    # op is one of +,*,)
    # b is either a literal or (
    # evaluate a op b for s = n*m or s = n+m and return [s] + expressionlist
    # ex: 1+2+3
    # ex   = [1,+,2,+,3]
    # a = 1, op = 2, b = 3
    # return [    3,+,3]

    while len(ex) > 1:
        # may only have 2 left if ex ends with closing parens
        if ex[1] == ')':
            if ex[2:] == []:
                return ex[0:1]
            else:
                return ex[0:1] + ex[2:]

        a,op,b = ex[0:3]
        # nested parens can lead to a being (
        # ex 1 + ((2 * 3) * 4)
        if a == '(':
            ex = eval_expr(ex[1:])
        elif b == '(':
            ex = [a,op] + eval_expr(ex[3:])
        elif op == '+':
            ans = int(a)+int(b)
            ex = [ans] + list(ex[3:])
        elif op == '*':
            ans = int(a)*int(b)
            ex = [ans] + list(ex[3:])
    return ex

def operate4(line):
    while len(line) > 1:
        print(line)
        if line[1] == ')':
            if line[2:] == []:
                return line[0:1]
            else:
                return line[0:1] + line[2:]
        if line[0] == '(':  # ( 0 +
            line = operate(line[1:])
        elif line[2:3] == '(': # 0 + (
            line = [line[0], line[1]] + operate(line[3:])
        elif line[1] == '+' or line[1] == '*': # 0 + 1
            op = line[1]
            a = int(line[0])
            b = int(line[2])
            result = a + b if op == '+' else a * b
            line = [result] + [line[3:]]
    return line


total = 0
'''
with open("inputEjemplo.txt") as file:
    for line in file:
        expression = []
        for symbol in line.rstrip().replace(' ', ''):
            if symbol.isnumeric():
                expression.append(int(symbol))
            else:
                expression.append(symbol)
        #result = operate(line.rstrip().replace(' ', ''))[0]
        result = operate(expression)[0]
        print(result)
        total += result
        #break

print(total)
'''
'''
def operate(acc):
    if acc[1] == ')':
        return
'''

'''
while len(ex) > 1:
    # may only have 2 left if ex ends with closing parens
    if ex[1] == ')':
        if ex[2:] == []:
            return ex[0:1]
        else:
            return ex[0:1] + ex[2:]

    a,op,b = ex[0:3]
    # nested parens can lead to a being (
    # ex 1 + ((2 * 3) * 4)
    if a == '(':
        ex = eval_expr(ex[1:])
    elif b == '(':
        ex = [a,op] + eval_expr(ex[3:])
    elif op == '+':
        ans = int(a)+int(b)
        ex = [ans] + list(ex[3:])
    elif op == '*':
        ans = int(a)*int(b)
        ex = [ans] + list(ex[3:])
return ex
'''

def operate(acc):
    ans = -1
    while len(acc) > 1:
        print(acc)
        if ans != -1:
            if acc[1] == ')':
                acc = [acc[0]] + acc[2:]
        if acc[1] == ')':
            acc = [acc[0]]# + acc[2:]
            #return operate(acc)
        elif acc[0] == '(':
            ans = operate(acc[1:])
        elif acc[0] != '+' or acc[0] != '*':
            a = acc[0]
            op = acc[1]
            b = operate(acc[2:])
            ans = a + b if op == '+' else a * b
            print(f'{a} {op} {b} = {ans}')
            acc = [ans] + acc[3:]
    return acc[0]

with open("inputEjemplo.txt") as file:
    for line in file:
        expression = []
        for symbol in line.rstrip().replace(' ', ''):
            if symbol.isnumeric():
                expression.append(int(symbol))
            else:
                expression.append(symbol)
        #result = operate(line.rstrip().replace(' ', ''))[0]
        exp = []
        j = 0
        for i in expression[::-1]:
            symbol = i
            if i == '(':
                symbol = ')'
            elif i == ')':
                symbol = '('
            exp.append(symbol)
        result = operate(exp)
        print(result)
        total += result
        break
    print("TOTAL:", total)
