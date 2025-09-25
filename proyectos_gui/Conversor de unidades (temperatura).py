from tkinter import *

root = Tk()
root.title("Conversor de unidades")

#---------------Funcion para convertir-------------
def convertir():
	try:
		valor = float(entrada.get())
		if opcion.get()==1:
			resultado.set(str(valor * 9/5 + 32) + " °F")
		else:
			resultado.set(str((valor-32) * 5/9) + " °C")
			
		entrada.delete(0, END)

	except:
		pass


#----------Seccion 1: Cabecera y botones de radio----------
frm1 = Frame(root)
frm1.pack(pady=10)

Label(frm1, text="Conversor de unidades", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

#Botones de radio
opcion = IntVar(value=1)
Radiobutton(frm1, text="Celsius a Farenheit", variable=opcion, value=1).grid(row=1, column=0)
Radiobutton(frm1, text="Farenheit a Celsius", variable=opcion, value=2).grid(row=1, column=1)

#-----------Seccion 2: Entrada, boton conversor y resultado-----------
frm2 = Frame(root)
frm2.pack(pady=10)

entrada = Entry(frm2)
entrada.grid(row=0, column=0, columnspan=2, pady=5)

Button(frm2, text="Convertir", command=lambda:convertir()).grid(row=1, column=0, columnspan=2, pady=5)

resultado = StringVar()
Label(frm2, textvariable=resultado).grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()