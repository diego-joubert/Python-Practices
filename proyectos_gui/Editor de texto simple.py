from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Editor de texto")

#----------Funciones: Abrir y Guardar----------
def abrir():
	archivo = filedialog.askopenfilename()

	if archivo:
		with open(archivo, "r") as f:
			texto.delete(1.0, END)
			texto.insert(END, f.read())

def guardar():
	archivo = filedialog.asksaveasfilename(defaultextension=".txt")

	if archivo:
		with open(archivo, "w") as f:
			f.write(texto.get(1.0, END))

#-----------------Menu-------------------
menu = Menu(root)
root.config(menu=menu)

archivo_menu = Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo_menu)

archivo_menu.add_command(label="Abrir", command=abrir)
archivo_menu.add_command(label="Guardar", command=guardar)

#----------------Texto----------------------
texto = Text(root, yscrollcommand=lambda: scrollbar.set)
texto.pack(expand=True, fill="both")

#----------------Scrollbar------------------
scrollbar = Scrollbar(root)
scrollbar.config(command=texto.yview)
scrollbar.pack()



root.mainloop()
