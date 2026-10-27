import random
import tkinter as tk
from tkinter import messagebox


class DesafioCanvas:
    def __init__(self, raiz):
        self.raiz = raiz
        self.cores = ["red", "blue", "green", "purple", "pink"]
        self.canvas = tk.Canvas(raiz, width=240, height=120)
        self.retangulo = self.canvas.create_rectangle(
            60, 20, 180, 100, fill="blue"
        )
        self.canvas.pack(pady=10)

        tk.Button(raiz, text="Mudar cor", command=self.mudar_cor).pack()
        tk.Button(raiz, text="Avisar", command=self.avisar).pack(pady=5)

    def mudar_cor(self):
        self.canvas.itemconfig(self.retangulo, fill=random.choice(self.cores))

    def avisar(self):
        messagebox.showinfo(
            "Aviso",
            "Este exemplo permite mudar a cor do retângulo.",
            parent=self.raiz,
        )


if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Mudar cor do retângulo")
    DesafioCanvas(raiz)
    raiz.mainloop()