count = 0

# Se abre el archivo
with open("inputDiana.txt") as file:
    # Por cada contraseña separamos la política (limite - letra) y
    # la contraseña respectiva
    for line in file:
        policy, password = line.rstrip().split(": ")
        limits, letter = policy.split(' ')
        pos1, pos2 = limits.split('-')
        # Comprobación de la letra en la posici+on especificada por la
        # política respectiva a la contraseña 
        if (password[int(pos1)-1] == letter) != (password[int(pos2)-1] == letter):
            count += 1

print("La cantidad de contraseñas válidas:", count)
