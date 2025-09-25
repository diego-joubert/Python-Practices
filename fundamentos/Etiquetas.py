from tkinter import Tk, Label

root = Tk()
etiqueta1 = Label( text="Arriba ")
etiqueta2 = Label( text="Abajo")
etiqueta3 = Label( text="Izquierda")
etiqueta4 = Label( text="Derecha")

etiqueta1.pack(side = "top",pady = 10)
etiqueta2.pack(side = "bottom",pady = 10)
etiqueta3.pack(side = "left", pady = 10)
etiqueta4 .pack(side = "right", pady = 10)
root.mainloop()