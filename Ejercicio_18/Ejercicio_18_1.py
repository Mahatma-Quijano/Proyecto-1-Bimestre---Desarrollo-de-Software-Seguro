def calculate(line):
    ans = 0
    i = 0
    op = ''
    while i < len(line):
        if line[i] == ')':
            return ans, i
        if line[i] in ['+', '*']:
            op = line[i]
        elif line[i].isnumeric():
            if ans == 0:
                ans = int(line[i])
            else:
                b = int(line[i])
                ans = ans * b if op =='*' else ans + b
        elif line[i] == '(':
            b, j = calculate(line[i+1:])
            ans = ans * b if op =='*' else ans + b
            i += j + 1
        i += 1
    return ans, i


total = 0
with open("inputDiana.txt") as file:
    for line in file:
        line = line.rstrip().replace('(', '( ')
        line = line.replace(')', ' )')
        expression = line.split()
        result, _ = calculate(expression)
        total += result

print("TOTAL:", total)
