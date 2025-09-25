import tkinter as tk

def out():
    frm = tk.Frame(root)
    frm.pack(pady=5, padx=5)

    tk.Label(frm, text="Desea salir?").pack(pady=5, padx=5)
    tk.Button(frm, text="Si", command= lambda : root.destroy()).pack(pady=5, padx=5)
    tk.Button(frm, text="No", command= lambda : frm.destroy()).pack(pady=5, padx=5)

root = tk.Tk()
salir = tk.Button(root, text="Salir", command = out)
salir.pack()
root.mainloop()