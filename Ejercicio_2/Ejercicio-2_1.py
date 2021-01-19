count = 0
with open("inputDiana.txt") as file:
    for line in file:
        policy, password = line.rstrip().split(": ")
        limits, letter = policy.split(' ')
        min, max = limits.split('-')
        number = password.count(letter)
        if (int(min) <= number) and (number <= int(max)):
            count += 1

print("La cantidad de contraseñas válidas:", count)
