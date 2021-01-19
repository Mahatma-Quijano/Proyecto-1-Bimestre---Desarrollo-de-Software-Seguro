import re # Importa la librería de Expresiones Regulares

# Método que calcula las operaciones de una expresion sin paréntesis
def calculate(line):
    ans, i, op = 0, 0, ''   # Variables iniciales
    while i < len(line):    # Mientras la línea tenga más de 1 símbolo
        flag = '+' not in line  # Bandera que indica que se acabaron las sumas
        if line[i] == '+':
            op = line[i]
        elif line[i] == '*':
            if flag: # Si ya no hay más sumas, continúa con las multiplicaciones
                op = line[i]
            else: # No toma en cuenta los números que deban multiplicarse
                ans = 0
        elif line[i].isnumeric():
            if ans == 0:    # Si el acumulador aún no ha sido actualizado
                ans = int(line[i])
            else:
                b = int(line[i])
                # Se realiza la operación
                if op == '+':
                    ans += b
                elif op == '*':
                    ans *= b
                # ------------------ Se acorta la expresión
                line[i] = str(ans)  # Se guarda el resultado
                del line[i-2:i]     # Se eliminan los dos símbolos anteriores
                ans = 0             # Indica que espera otro número para operar
                i -= 3              # Retrocede el iterador
        i += 1
        # La primera vez que se terminen las sumas
        if '+' not in line and not flag:
            i = 0   # El iterador vuelve al inicio para empezar con las multiplicaciones
    return ans, i

def operate(exp):
    parenth = re.findall("\([0-9]+[^()]+\)", exp)
    while len(parenth) >= 1:
        for p in parenth:
            content = re.findall("([0-9]+|[+*])", p)
            result, i = calculate(content)
            exp = exp.replace(p, str(result), 1)
        parenth = re.findall("\([0-9]+[^()]+\)", exp)
    content = re.findall("([0-9]+|[+*])", exp)
    return calculate(content)

total = 0
with open("inputMahatma.txt") as file:
    for line in file:
        expression = line.replace(' ', '')
        result, _ = operate(expression)
        total += result

print("TOTAL:", total)
