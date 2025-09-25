from tkinter import *

raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

archivo = open("fuentes.txt", "r")

fuentes = list(archivo.read().split("\n"))

for i in range(len(fuentes)):
    Label(miFrame, text=f"Etiqueta {i+1}", font=(fuentes[i], 14)).pack(pady=10)


raiz.mainloop()