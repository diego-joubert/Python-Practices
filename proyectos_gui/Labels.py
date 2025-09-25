import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Labels en Tkinter")

# Label básico
label1 = ttk.Label(root, text="Etiqueta simple")
label1.pack(pady=5)

# Label con formato
label2 = ttk.Label(root, 
                   text="Etiqueta con formato",
                   font=("Arial", 12, "bold"),
                   foreground="blue",
                   background="#f0f0f0",
                   padding=10)
label2.pack(pady=5)

# Label con imagen
try:
    imagen = tk.PhotoImage(file="icono.png", height="100")  # Cambia por tu ruta de imagen
    label3 = ttk.Label(root, image=imagen, text="Logo", compound="right")
    label3.pack(pady=5)
except:
    label3 = ttk.Label(root, text="Imagen no encontrada")
    label3.pack(pady=5)

# Label con texto dinámico
texto_var = tk.StringVar(value="Texto dinámico")
label4 = ttk.Label(root, textvariable=texto_var)
label4.pack(pady=5)

def cambiar_texto():
    texto_var.set("¡Texto cambiado!")

ttk.Button(root, text="Cambiar texto", command=cambiar_texto).pack(pady=5)

root.mainloop()