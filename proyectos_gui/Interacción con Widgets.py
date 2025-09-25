import tkinter as tk
from tkinter import messagebox

# Función para manejar el clic en el botón
def on_button_click():
    texto = entrada.get()
    messagebox.showinfo("Mensaje", f"Has escrito: {texto}")

# Función para manejar el evento de presionar Enter en la entrada de texto
def on_enter_press(event):
    on_button_click()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interacción con Widgets")
ventana.geometry("400x200")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Escribe algo y presiona Enter o haz clic en el botón:")
etiqueta.pack(pady=10)

# Crear una entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Capturar el evento de presionar Enter en la entrada de texto
entrada.bind("<Return>", on_enter_press)

# Crear un botón
boton = tk.Button(ventana, text="Mostrar Mensaje", command=on_button_click)
boton.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()