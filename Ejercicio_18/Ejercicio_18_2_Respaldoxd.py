import re

def calculateMEDIOFUNCIONAL(line):
    #AAAprint(" Calculate ", line)
    ans = 0
    i = 0
    op = ''
    flag = False
    while i < len(line):
        #AAAprint("i:", i, "\tans:", ans, "\top:", op)
        #if line[i] == ')':
        #    return ans, i
        if line[i] == '+':
            op = line[i]
        elif line[i] == '*':# and flag:
            if flag:
                op = line[i]
            else:
                ans = 0
            #AAAprint("\tNEW:", op)
        elif line[i].isnumeric():
            if ans == 0:
                ans = int(line[i])
            elif op != '':
                a = ans
                b = int(line[i])
                #ans = ans * b if op =='*' else ans + b
                if op == '+':
                    ans += b
                elif op == '*':
                    ans *= b
                #AAAprint(f'{line[i]}:\t', f'{a} {op} {b} = {ans}')
                if '*' in line and not flag: # Que se encargue de todas las Sumas primero
                    #AAAprint("\tBorrar", line[i-2:i])
                    #AAAprint("\tReemplazar siguiente", str(ans))
                    line[i] = str(ans)
                    #for s in line[i-2:i]:
                    #    line.remove(s)
                    del line[i-2:i]
                    #AAAprint("\t", line)
                    ans = 0
                    i -= 3

        #elif line[i] == '(':
        #    a = ans
        #    b, j = calculate(line[i+1:])
        #    ans = ans * b if op =='*' else ans + b
        #    #AAAprint("(:\t", f'{a} {op} {b} = {ans}', "\t\t", line)
        #    #AAAprint("\t\tJ:", j)
        #    i += j + 1

        i += 1
        #if i == len(line) and len(line) == 1:
        #    i = 0
        #if '+' not in line and i == len(line) and not flag:
        if '+' not in line and not flag:
            i = 0
            flag = True
    return ans, i

'''
def calculate2(line):
    #AAAprint(" Calculate ", line)
    ans = 0
    i = 0
    op = ''
    flag = False
    while i < len(line):
        #AAAprint("i:", i, "\tans:", ans, "\top:", op)
        if line[i] == '+':
            op = line[i]
        elif line[i] == '*':
            if '+' not in line:
                op = '*'
            else:
                ans = 0
                #AAAprint("\tSalto el *:", i, " ans:", ans)
        elif line[i].isnumeric():
            if ans == 0:
                ans = int(line[i])
            else: #if op != '':
                a = ans
                b = int(line[i])
                #ans = ans * b if op =='*' else ans + b
                #if op == '+':
                #    ans += b
                ans = ans * b if op == '*' else ans + b
                #elif op == '*':
                #    ans *= b
                #AAAprint(f'{line[i]}:\t', f'{a} {op} {b} = {ans}')
                #if '*' in line and not flag: # Que se encargue de todas las Sumas primero
                #AAAprint("\tBorrar", line[i-2:i])
                #AAAprint("\tReemplazar lo siguiente", line[i], " con", ans)
                line[i] = str(ans)
                del line[i-2:i]
                #AAAprint("\t", line)
                ans = 0
                if '+' in line:
                    i -= 2
                else:
                    i = -1
        #else: #if '*' in line:

        i += 1
        #if i == len(line) and len(line) == 1:
        #    i = 0
        #if '+' not in line and i == len(line) and not flag:
        if '+' not in line and not flag:
            #AAAprint("\tste If xd")
            i = 0
            flag = True
    return ans, i
def calculate3(line):
    #AAAprint(" Calculate ", line)
    ans = 0
    i = 0
    op = ''
    flag = False
    while i < len(line):
        flag = '+' not in line
        #AAAprint("i:", i, "\tans:", ans, "\top:", op)
        if line[i] == '+':
            op = line[i]
        elif line[i] == '*':
            if flag:
                op = '*'
            else:
                ans = 0
                #AAAprint("\tSalto el *:", i, " ans:", ans)
        elif line[i].isnumeric():
            if ans == 0:
                ans = int(line[i])
            else:
                a = ans
                b = int(line[i])
                ans = ans * b if op == '*' else ans + b
                #AAAprint(f'{line[i]}:\t', f'{a} {op} {b} = {ans}')
                #AAAprint("\tBorrar", line[i-2:i])
                #AAAprint("\tReemplazar lo siguiente", line[i], " con", ans)
                line[i] = str(ans)
                del line[i-2:i]
                #AAAprint("\t", line)
                ans = 0
                if '+' in line:
                    i -= 2
                else:
                    i = -1
        i += 1
        if '+' not in line and not flag:
            #AAAprint("\tste If xd")
            i = 0
            flag = True
    return ans, i
'''

def calculate(line):
    #AAAprint(" Calculate ", line)
    ans = 0
    i = 0
    op = ''
    flag = False
    while i < len(line):
        flag = '+' not in line
        #AAAprint("i:", i, "\tans:", ans, "\top:", op)
        #if line[i] == ')':
        #    return ans, i
        if line[i] == '+':
            op = line[i]
        elif line[i] == '*':# and flag:
            if flag:
                op = line[i]
            else:
                ans = 0
            #AAAprint("\tNEW:", op)
        elif line[i].isnumeric():
            if ans == 0:
                ans = int(line[i])
            elif op != '':
                a = ans
                b = int(line[i])
                #ans = ans * b if op =='*' else ans + b
                if op == '+':
                    ans += b
                elif op == '*':
                    ans *= b
                #AAAprint(f'{line[i]}:\t', f'{a} {op} {b} = {ans}')
                #if '*' in line and not flag: # Que se encargue de todas las Sumas primero
                #AAAprint("\tBorrar", line[i-2:i])
                #AAAprint("\tReemplazar siguiente", str(ans))
                line[i] = str(ans)
                #for s in line[i-2:i]:
                #    line.remove(s)
                del line[i-2:i]
                #AAAprint("\t", line)
                ans = 0
                i -= 3

        i += 1
        if '+' not in line and not flag:
            i = 0
            flag = True
    return ans, i


# TODO que no reciba la lista sino solo el string...
def operate(exp):
    string = ''.join(map(str, exp))
    parenth = re.findall("\([0-9]+[^()]+\)", string)
    while len(parenth) >= 1:#'(' in exp:
        #AAAprint(string, "--------------------------------------------------")
        #AAAprint("PARENTH", parenth)
        for p in parenth:
            content = re.findall("([0-9]+|[+*])", p)
            #result, _ = calculate(list(p)[1:-1])
            result, i = calculate(content)
            #AAAprint("\tEnded at", i)
            #AAAprint("\tResultado de", p, ":", result)
            #string = re.sub("\([0-9]+[^()]+\)", str(result), string, 1)
            #AAAprint("\tReemplazar", p, " con ", str(result))
            #string = re.sub(p, str(result), string, 1)
            string = string.replace(p, str(result), 1)
            #AAAprint("\tNuevo String:", string)
        exp = list(string)
        parenth = re.findall("\([0-9]+[^()]+\)", string)
    #AAAprint("\tno hay mas parentesis !!!")
    content = re.findall("([0-9]+|[+*])", string)
    return calculate(content)

total = 0
with open("inputMahatma.txt") as file:
    for line in file:
        line = line.rstrip().replace('(', '( ')
        line = line.replace(')', ' )')
        #AAAprint("\n------- ", line, "||||||||||||||||||||||||||||||||||||||||")
        expression = line.split()
        result, _ = operate(expression)
        #AAAprint("\t\t\t\t\t\tRESULT:", result, "\n")
        total += result
        #break

print("TOTAL:", total)

#AAAprint("Deberia dar:", 694173)
