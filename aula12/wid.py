import tkinter as tk
from tkinter import ttk

class EventoApp:
    def __init__(self, raiz):
        raiz.title("Evento de botão")
        self.label = ttk.Label(raiz, text = "Olá, Tkinter")
        self.label.pack(pady = 0)
        botao == ttk.Button(raiz, text = "Clique em mim", comand = self.clicado)
        boao.pack(pady = 0)

    def clicado(self):
        self.label.config(text="Botão clicado")

if __name__ == "__main__":
    raiz = tk.Tk()
    EventoApp(raiz)
    raiz.mainloop()