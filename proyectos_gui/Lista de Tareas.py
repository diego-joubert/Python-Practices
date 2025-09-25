from tkinter import *

root = Tk()
root.title("Lista de Tareas")

#--------Funciones------------
def agregar_tarea():
	tarea = entrada.get()

	if tarea and tarea not in lista_tareas.get(0, END):
		lista_tareas.insert(END, tarea)
		entrada.delete(0, END)
		info.set("Tarea agregada con exito :D")


def eliminar_tarea():
	tarea = lista_tareas.curselection()[0]

	try:
		lista_tareas.delete(tarea)
		info.set("Tarea eliminada con exito")
	except IndexError:
		info.set("Ha ocurrido un error al eliminar la tarea, intente de nuevo")
	

#--------Frame superior-------
frm = Frame(root)
frm.grid(row=0, column=0, columnspan=2)

#--------Label para notificar---------
info = StringVar()
estado = Label(frm, text="", textvariable=info)
estado.grid(row=2, column=0, columnspan=2)


#--------Pantalla----------
entrada = Entry(frm, width="40")
entrada.grid(row=0, column=0, columnspan=2, pady="10")

#--------Botones-----------
agregar = Button(frm, text="Agregar tarea", command=lambda: agregar_tarea())
agregar.grid(row=1, column=0)

eliminar = Button(frm, text="Eliminar tarea", command=lambda: eliminar_tarea())
eliminar.grid(row=1, column=1)

#--------Lista-------------
lista_tareas = Listbox(root, width=100, height=20, selectbackground="lightblue", yscrollcommand=lambda:scrollbar.set)
lista_tareas.grid(row=1, column=0, pady=10, padx=10)

#Scrollbar vertical
scrollbar = Scrollbar(root)
scrollbar.config(command=lista_tareas.yview)
scrollbar.grid(row=1, column=1, sticky="nsew")

root.mainloop()
