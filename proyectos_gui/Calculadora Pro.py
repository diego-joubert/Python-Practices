import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        # Variable para almacenar el resultado
        self.resultado = tk.StringVar()
        self.resultado.set("0")
        
        # Pantalla de resultado
        pantalla = ttk.Entry(root, textvariable=self.resultado, 
                            justify="right", font=("Arial", 14), state="readonly")
        pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row, col = 1, 0
        for btn in botones:
            ttk.Button(root, text=btn, command=lambda b=btn: self.click(b)).grid(
                row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configurar el peso de las filas y columnas
        for i in range(5):
            root.rowconfigure(i, weight=1)
        for i in range(4):
            root.columnconfigure(i, weight=1)
    
    def click(self, tecla):
        if tecla == "C":
            self.resultado.set("0")
        elif tecla == "=":
            try:
                expr = self.resultado.get()
                res = str(eval(expr))
                self.resultado.set(res)
            except:
                self.resultado.set("Error")
        else:
            if self.resultado.get() == "0" or self.resultado.get() == "Error":
                self.resultado.set(tecla)
            else:
                self.resultado.set(self.resultado.get() + tecla)

# Crear y ejecutar la calculadora
root = tk.Tk()
app = Calculadora(root)
root.mainloop()