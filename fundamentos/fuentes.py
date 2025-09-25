from tkinter import Tk, font
raiz = Tk()

archivo = open("fuentes.txt", "w")
fuentes = list(font.families())

for fuente in fuentes:
    archivo.write(f"{fuente} \n")