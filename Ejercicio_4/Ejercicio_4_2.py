import re
archivo = "inputDiana.txt"

# Diccionario con las validaciones requeridas para cada campo
requiredFields = {
    "byr": (4, 1920, 2002),
    "iyr": (4, 2010, 2020),
    "eyr": (4, 2020, 2030),
    "hgt": [(150, 193, "cm"), (59, 76, "in")],
    "hcl": '#[0-9a-f]{6}$',
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": '[0-9]{9}$'
}

# Valores globales que van a ser usados mas adelante
requiredNumber = len(requiredFields)
pasaportesValidos = 0

# Función que comprueba los años de los campos BYR, IYR y EYR
def year(value, field, requiredFields):
    digitos, min, max = requiredFields[field]
    if re.match("[0-9]{4}", value):
        if (min <= int(value)) and (int(value) <= max):
            return True
    return False

# Función que verifica las médidas del campo HGT
def measure(value, requiredFields):
    if re.match("[0-9]{3}cm", value):
        medida = value.split('c')[0]
        min = requiredFields["hgt"][0][0]
        max = requiredFields["hgt"][0][1]
        if (min <= int(medida)) and (int(medida) <= max):
            return True
    elif re.match("[0-9]{2}in", value):
        medida = value.split('i')[0]
        min = requiredFields["hgt"][1][0]
        max = requiredFields["hgt"][1][1]
        if (min <= int(medida)) and (int(medida) <= max):
            return True
    return False

# Se abre el archivo
with open(archivo) as file:
    # Proceso por cada Pasaporte
    for i, line in enumerate(file):
        passportFields = dict()
        # Lee las líneas siguientes hasta encontrar una línea en blanco (siguiente Pasaporte)
        while (line != '\n') and (len(line) != 0):
            # Obtiene cada par clave:valor de una línea
            info = line.rstrip().split(' ')
            # Separa y almacena los campos del Pasaporte
            for data in info:
                passportFields[data.split(':')[0]] = data.split(':')[1]
            # Lee la siguiente línea
            line = file.readline()
        # Comprueba que cada uno de los campos dentro del Pasaporte cumplan las reglas
        validFields = 0
        for field in passportFields:
            valid = False
            if field in requiredFields:
                if field == "byr" or field == "iyr" or field == "eyr":
                    valid = year(passportFields[field], field, requiredFields)
                elif field == "hgt":
                    valid = measure(passportFields[field], requiredFields)
                elif field == "hcl" or field == "pid":
                    valid = bool(re.match(requiredFields[field], passportFields[field]))
                elif field == "ecl":
                    valid = passportFields[field] in requiredFields[field]
            # El campo CID se considera siempre válido
            elif field == "cid":
                valid = True
            # Se cuentan los campos válidos
            if valid:
                if not field == "cid":
                    validFields += 1
            else:
                break # Si un campo no es válido, el Pasaporte tampoco lo es
        # Si todos los campos son válidos, se cuenta como Pasaporte Válido
        if validFields == requiredNumber:
            pasaportesValidos += 1

print("Pasaportes Válidos:", pasaportesValidos)
