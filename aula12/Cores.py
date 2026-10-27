import random
import tkinter as tk

class CoresApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.cores = ["red", "blue", "green", "puple", "pink"]
        raiz.title("Janela divertida")
        raiz.geometry("300x200")
        tk.Label(raiz, text = "Janela Sobre!", font = ("Arial", 14)).pack(pady = 10)

    def mudar_cor(self):
        self.raiz.config(bg = random.choice(self.cores))

if __name__ == "__main__":
    raiz = tk.Tk()
    CoresApp(raiz)
    raiz.mainloop()