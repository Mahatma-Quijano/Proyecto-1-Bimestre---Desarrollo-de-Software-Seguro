# Se crea una lista del reporte en blanco
expenseReport = []

# Se abre y se coloca los elementos del archivo en la lista
with open("inputDiana.txt") as file:
    for line in file:
        expenseReport.append(int(line.rstrip()))

# Se ordena la lista y obtenemos su longitud
expenseReport.sort()
length = len(expenseReport)

# Se crea una función de busqueda binaria
def find(num, min, max, lista):
    medio = (min + max) // 2
    if min > max:
        return False
    if num < lista[medio]:
        max = medio - 1
    elif num > lista[medio]:
        min = medio + 1
        find(num, medio + 1, max, lista)
    elif num == lista[medio]:
        return True
    return find(num, min, max, lista)

# Se itera por cada número del reporte, para ver que valor sumado a este
# da como resultado 2020, para posteriormente aplicar busqueda binaria y
# comprobar su existencia en la lista del reporte
for num1 in expenseReport:
    num2 = 2020 - num1
    found = find(num2, 0, length-1, expenseReport)
    if found:
        print("Primer número:", num1, "Segundo número:", num2, "Suma:", num1+num2, "Multiplicación:", num1*num2)
        break
