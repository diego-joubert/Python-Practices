f = open("archivo.txt", "w")

contenido = ["a", "1", "π", "hola", "Python :)"]
f = f.writelines(contenido)
f.read()