from tkinter import *
import time

root = Tk()
root.title("Reloj digital")

def actualizar_hora():
	hora_actual = time.strftime("%H:%M:%S")
	hora.set(hora_actual)
	root.after(1000, actualizar_hora)

hora = StringVar()
Label(root, textvariable=hora).pack(pady=20)

actualizar_hora()
root.mainloop()
