from tkinter import *

raiz = Tk()

cuadroTexto = Entry(raiz).grid(row=0, column=1)

miLabel = Label(raiz, text="Nombre:").grid(row=0, column=0)


raiz.mainloop()