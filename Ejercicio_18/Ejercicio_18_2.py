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
    return ans

# Método que se encarga de obtener los resultados de la expresión
# yendo desde los paréntesis más internos hacia afuera
def operate(exp):
    # Obtiene una lista con los paréntesis interno
    parenth = re.findall("\([0-9]+[^()]+\)", exp)
    # Mientras hayan paréntesis
    while len(parenth) >= 1:
        # Por cada paréntesis interno
        for p in parenth:
            # Se obtiene una lista con los números y operadores dentro del paréntesis
            content = re.findall("([0-9]+|[+*])", p)
            # Se calcula el resultado del contenido
            result = calculate(content)
            # Se reemplaza el resultado de la expresión con paréntesis
            exp = exp.replace(p, str(result), 1)
        # Busca la siguiente lista de expresiones entre paréntesis
        parenth = re.findall("\([0-9]+[^()]+\)", exp)
    # Se obtiene la expresión final y se opera
    content = re.findall("([0-9]+|[+*])", exp)
    return calculate(content)

total = 0
# Se obtienen las expresiones del archivo de entrada
with open("inputMahatma.txt") as file:
    for line in file:
        # Se eliminan los espacios en blanco
        expression = line.replace(' ', '')
        # Se obtiene el resultado de cada expresión y se acumula
        result = operate(expression)
        total += result

print("TOTAL:", total)
