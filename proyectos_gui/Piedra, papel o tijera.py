from tkinter import *
import random

def jugar(opc_usuario):
	opciones = ["Piedra", "Papel", "Tijeras"]
	opc_pc = random.choice(opciones)

	if opc_usuario==opc_pc:
		resultado.set(f"Empate! La PC tambien eligio {opc_pc}")

	elif (opc_usuario=="Piedra" and opc_pc=="Tijeras") or (opc_usuario=="Papel" and opc_pc=="Piedra") or (opc_usuario=="Tijeras" and opc_pc=="Papel") :
		resultado.set(f"Ganaste! {opc_usuario} gana a {opc_pc}")

	
	else:
		resultado.set(f"Perdiste! La PC eligio {opc_pc}")

root = Tk()
root.title("Piedra, Papel o Tijeras")

resultado = StringVar()
Label(root, textvariable=resultado).pack(pady=10, padx=10)

Button(root, text="Piedra", command=lambda:jugar("Piedra")).pack(padx=5)
Button(root, text="Papel", command=lambda:jugar("Papel")).pack(padx=5)
Button(root, text="Tijeras", command=lambda:jugar("Tijeras")).pack(padx=5)


root.mainloop()
