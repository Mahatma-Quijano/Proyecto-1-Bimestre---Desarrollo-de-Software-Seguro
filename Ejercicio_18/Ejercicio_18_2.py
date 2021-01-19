import re

def calculate2(line):
    ans, i, op = 0, 0, ''
    while i < len(line):
        flag = '+' not in line
        if line[i] == '+':
            op = line[i]
        elif line[i] == '*':
            if flag:
                op = line[i]
            else:
                ans = 0
        elif line[i].isnumeric():
            if ans == 0:
                ans = int(line[i])
            elif op != '':
                a = ans
                b = int(line[i])
                if op == '+':
                    ans += b
                elif op == '*':
                    ans *= b
                line[i] = str(ans)
                del line[i-2:i]
                ans = 0
                i -= 3

        i += 1
        '''
        if '+' not in line:
            i = 0
        '''
        if '+' not in line and not flag:
            i = 0

    return ans, i

def calculate(line):
    ans, i, op = 0, 0, ''
    while i < len(line):
        flag = '+' not in line
        if line[i] == '+':
            op = line[i]
        elif line[i] == '*':
            if flag:
                op = line[i]
            else:
                ans = 0
        elif line[i].isnumeric():
            if ans == 0:
                ans = int(line[i])
            elif op != '':
                a = ans
                b = int(line[i])
                if op == '+':
                    ans += b
                elif op == '*':
                    ans *= b
                line[i] = str(ans)
                del line[i-2:i]
                ans = 0
                i -= 3
        i += 1
        if '+' not in line and not flag:
            i = 0

    return ans, i



# TODO que no reciba la lista sino solo el string...
def operate(exp):
    string = ''.join(map(str, exp))
    parenth = re.findall("\([0-9]+[^()]+\)", string)
    while len(parenth) >= 1:
        for p in parenth:
            content = re.findall("([0-9]+|[+*])", p)
            result, i = calculate(content)
            string = string.replace(p, str(result), 1)
        exp = list(string)
        parenth = re.findall("\([0-9]+[^()]+\)", string)
    content = re.findall("([0-9]+|[+*])", string)
    return calculate(content)

total = 0
with open("inputDiana.txt") as file:
    for line in file:
        line = line.rstrip().replace('(', '( ')
        line = line.replace(')', ' )')
        expression = line.split()
        result, _ = operate(expression)
        total += result

print("TOTAL:", total)
