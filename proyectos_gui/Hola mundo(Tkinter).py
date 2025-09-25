from tkinter import Tk, Label, font
import random as r

root = Tk()

fuentes = list(font.families())
fuente = r.choice(fuentes)
tam = str(r.randint(10, 30))

etiqueta = Label(text = "Hola mundo! ", padx = 10, pady = 10, bg = "cyan", fg = "crimson", font = (fuente, tam, "bold italic"))

etiqueta.pack(expand = True, padx = 10, pady = 10, ipadx = 10, ipady = 10, fill = "both")

root.mainloop()