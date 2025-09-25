from tkinter import Tk, Label, Button, Entry

class Root(Tk):
    def __init__(self):
        super().__init__()
        
        self.titulo = Label(self, text="Esta es una calculadora simple \n No es para uso productivo")
        self.titulo.pack()
        self.entrada = Entry(self)
        self.entrada.pack()
        self.entrada.insert(0, "")
        self.salida = Label(self, text="")
        self.salida.pack()
        self.boton = Button(self, text="Calcular", command=self.click)
        self.boton.pack()
        
    def click(self):
        self.salida.configure(text=str(eval(self.entrada.get())))
        
raiz = Root()
raiz.mainloop()       