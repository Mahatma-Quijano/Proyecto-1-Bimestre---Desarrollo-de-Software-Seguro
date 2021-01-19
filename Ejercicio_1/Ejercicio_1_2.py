# Se crea una lista del reporte en blanco
expenseReport = []

# Se abre y se coloca los elementos del archivo en la lista
with open("inputMahatma.txt") as file:
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

# Se itera por cada par de números del reporte, para ver que valor sumado a estos
# da como resultado 2020. Luego se aplica busqueda binaria y
# se comprueba su existencia en la lista del reporte
for i in range(0, length):
    num1 = expenseReport[i]
    for j in range(i+1, length):
        num2 = expenseReport[j]
        num3 = 2020 - num1 - num2
        found = find(num3, 0, length-1, expenseReport)
        if found:
            print("Número 1:", num1, "Número 2:", num2, "Número 3:", num3, "Suma:", num1+num2+num3, "Multiplicación:", num1*num2*num3)
            break
    if found:
        break
