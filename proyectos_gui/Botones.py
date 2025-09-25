import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Botones en Tkinter")
root.geometry("400x300")

# Botón básico
def accion_basica():
    messagebox.showinfo("Información", "Botón presionado")

boton1 = ttk.Button(root, text="Botón simple", command=accion_basica)
boton1.pack(pady=5)

# Botón con estado deshabilitado
boton2 = ttk.Button(root, text="Deshabilitado", state="disabled")
boton2.pack(pady=5)

# Botón que cambia propiedades
def cambiar_boton():
    boton3.config(text="¡Cambiado!", state="disabled")

boton3 = ttk.Button(root, text="Cámbiame", command=cambiar_boton)
boton3.pack(pady=5)

# Botones con diferentes estilos
style = ttk.Style()
style.configure('TButton', font=('Arial', 10))
style.configure('Rojo.TButton', foreground='red', font=('Arial', 12, 'bold'))
style.configure('Verde.TButton', foreground='green')

boton4 = ttk.Button(root, text="Estilo rojo", style='Rojo.TButton',
                   command=lambda: print("Botón rojo"))
boton4.pack(pady=5)

boton5 = ttk.Button(root, text="Estilo verde", style='Verde.TButton',
                   command=lambda: print("Botón verde"))
boton5.pack(pady=5)

root.mainloop()