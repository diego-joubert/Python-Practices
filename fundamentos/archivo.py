f = open("archivo.txt", "r")
while True:
    linea = f.readline()
    if not linea:
        break
    print(linea)