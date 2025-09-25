from tkinter import Tk, Button
import random as r

root = Tk()
colores = ["yellow", "red", "blue", "green", "gray", "brown", "pink", "violet", "crimson"]
filas, columnas = r.randint(2, 10), r.randint(2, 10)

for fila in range(filas):
    for columna in range(columnas):
        etiqueta = Button(text = f"Etiqueta {fila+1}-{columna+1}", bg = r.choice(colores))
        etiqueta.grid(row = fila, column = columna, padx = 10, pady = 10)

root.mainloop()