import os

# Este metodo no vale xd (no le terminé)
def buscarConFuerzaBruta():
    with open("input.txt") as file:
        longitud = len(file.readline().rstrip())
        x = 0
        try:
            while(true):
                x += 3
                file.seek(3, os.SEEK_CUR)
                print(file.tell())
        except:
            print("lpm")

# Crear el mapa completo
def crearMapaCompleto():
    escritura = open("mapaCompleto.txt", 'w')
    with open("input.txt") as file:
        for line in file:
            linea = line.strip()
            for i in range(32):
                escritura.write(linea)
            escritura.write('\n')
    escritura.close()
