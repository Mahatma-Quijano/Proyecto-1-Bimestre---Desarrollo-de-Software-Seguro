# Variables globales que van a ser utilizadas a lo largo del código
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"]
requiredNumber = len(requiredFields)
pasaportes = {}
validos = 0

# Se abre el archivo
with open("inputDiana.txt") as file:
    # Proceso por cada Pasaporte
    for i, line in enumerate(file):
        info = []
        # El \n indica un nuevo pasaporte y el != 0 el fin del archivo
        while (line != '\n') and (len(line) != 0):
            info.extend(line.rstrip().split(' '))
            nextLine = file.readline()
            if nextLine != '\n':
                line = nextLine
            else:
                break
        # Comprobar la existencia del campo en la lista de requiredFields
        for data in info:
            field = data.split(':')[0]
            # Si existe sube el contador
            if field in requiredFields:
                pasaportes[f'{i}'] = pasaportes.get(f'{i}', 0) + 1
        # Si el pasaporte tiene los 7 campos requeridos, es válido
        if pasaportes[f'{i}'] == requiredNumber:
            validos += 1

print("Pasaportes Válidos:", validos)
