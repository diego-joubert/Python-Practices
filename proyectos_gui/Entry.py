import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry en Tkinter")

# Entry básico
entry1 = ttk.Entry(root)
entry1.pack(pady=5)

# Entry con placeholder
def on_focus_in(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(foreground='black')

def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(foreground='grey')

placeholder_text = "Ingrese su nombre"
entry2 = ttk.Entry(root, foreground='grey')
entry2.insert(0, placeholder_text)
entry2.bind("<FocusIn>", lambda e: on_focus_in(entry2, placeholder_text))
entry2.bind("<FocusOut>", lambda e: on_focus_out(entry2, placeholder_text))
entry2.pack(pady=5)

# Entry con validación
def validar_numero(char):
    return char.isdigit() or char == ""

validacion = root.register(validar_numero)
entry3 = ttk.Entry(root, validate="key", validatecommand=(validacion, '%S'))
entry3.pack(pady=5)
ttk.Label(root, text="Solo números").pack()

# Entry con texto oculto (para contraseñas)
entry4 = ttk.Entry(root, show="*")
entry4.pack(pady=5)
ttk.Label(root, text="Campo de contraseña").pack()

# Mostrar contenido del Entry
def mostrar_contenido():
    contenido = entry1.get()
    ttk.Label(root, text=f"Contenido: {contenido}").pack(pady=5)

ttk.Button(root, text="Mostrar contenido", command=mostrar_contenido).pack(pady=10)

root.mainloop()