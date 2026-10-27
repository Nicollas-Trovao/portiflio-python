from tkinter import Tk
from pathlib import Path


janela = Tk()
janela.title("Nós não mamamos o Python")

largura = 600
altura = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela - largura) // 2
y = (altura_tela - altura) // 2

janela.geometry(f"{largura}x{altura}+{x}+{y}")
icone = Path(__file__).with_name("icon.ico")

if icone.exists():
    janela.iconbitmap(str(icone))

janela.mainloop()