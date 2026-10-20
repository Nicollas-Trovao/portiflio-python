import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, raiz):
        self.label = ttk.Label(raiz, text="Pronto!")
        self.label.pack(pady=12)
        ttk.Button(raiz, text="Clique", command = self.clicar).pack()

    def clicar(self):
        self.label.config(text = "Você clicou!")

if __name__ == "__main__":
    raiz = tk.Tk()
    App(raiz)
    raiz.mainloop()

class GradeApp:
    def __init__(self, raiz):
        raiz.title("Exemplo de sticky")
        raiz.columnconfigure(0, minsize = 250)
        raiz.rowconfigure((0, 1), minsize = 100)
        a = tk.Label(raiz, text = "A", bg = "red", fg = "white")
        a.grid(row = 0, column = 0, sticky = "ne")
        b = tk.Label(raiz, text = "B", bg = "blue", fg = "White")
        b.grid(row = 1, column = 0, sticky = "sw")

if __name__ == "__main__":
    raiz = tk.Tk()
    GradeApp(raiz)
    raiz.mainloop()