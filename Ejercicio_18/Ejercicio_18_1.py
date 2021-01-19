# Método que realiza el cálculo de izquierda a derecha
def calculate(line):
    ans = 0 # Acumulador del resultado
    i = 0   # Iterador
    op = '' # Operador
    while i < len(line): # Mientras la línea tenga más de 1 símbolo
        if line[i] == ')':
            return ans, i # Retorna el valor acumulado y la última posición del iterador
        if line[i] in ['+', '*']:
            op = line[i] # Almacena el operador
        elif line[i].isnumeric():
            if ans == 0: # Si el acumulador aún no ha sido actualizado
                ans = int(line[i])
            else:
                b = int(line[i])
                ans = ans * b if op == '*' else ans + b # Se actualiza el resultado
        elif line[i] == '(': # Con cada paréntesis se utiliza recursividad
            b, j = calculate(line[i+1:])
            ans = ans * b if op == '*' else ans + b
            i += j + 1 # El iterador se actualiza a la posición al finalizar el paréntesis
        i += 1
    return ans, i # Retorna el valor acumulado y la última posición del iterador


total = 0
# Se obtienen los datos del archivo de entrada
with open("inputDiana.txt") as file:
    for line in file:
        # Se añaden espacios a los paréntesis
        # de manera que cada signo esté separado por espacios
        line = line.rstrip().replace('(', '( ')
        line = line.replace(')', ' )')
        # Se crea una lista de todos los símbolos
        expression = line.split()
        # Se obtiene el cálculo
        result, _ = calculate(expression)
        # Se acumula la suma de cada resultado
        total += result

print("TOTAL:", total)
