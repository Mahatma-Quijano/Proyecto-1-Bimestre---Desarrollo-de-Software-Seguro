count = 0

# Se abre el archivo
with open("inputDiana.txt") as file:
    # Por cada contraseña separamos la política (limite - letra) y
    # la contraseña respectiva
    for line in file:
        policy, password = line.rstrip().split(": ")
        limits, letter = policy.split(' ')  # Límite - letra
        min, max = limits.split('-')
        # Contamos la cantidad de letras indicada en la política
        number = password.count(letter)
        # Comprobar si esta dentro de los límites de la política
        if (int(min) <= number) and (number <= int(max)):
            count += 1

print("La cantidad de contraseñas válidas:", count)
