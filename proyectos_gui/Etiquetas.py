from tkinter import Tk, Label

root = Tk()
etiqueta1 = Label( text="Arriba ")
etiqueta2 = Label( text="Abajo")
etiqueta3 = Label( text="Izquierda")
etiqueta4 = Label( text="Derecha")

etiqueta1.pack(side = "top", padx = 10, pady = 5)
etiqueta2.pack(side = "bottom", padx = 10, pady = 5)
etiqueta3.pack(side = "left", padx = 10, pady = 5)
etiqueta4 .pack(side = "right", padx = 10, pady = 5)
root.mainloop()