import tkinter as tk
from tkinter import messagebox


def main():
    janela = tk.Tk()
    janela.title("Brincando com Tkinter")
    janela.resizable(False, False)

    def mostrar_nome():
        nome = entrada_nome.get().strip()

        if nome:
            messagebox.showinfo("Cadastro", f"Olá, {nome}!")
            return

        messagebox.showwarning("Atenção", "Informe seu nome.")

    tk.Label(
        janela,
        text="Digite seu nome:",
        foreground="red",
        background="black",
        padx=12,
        pady=10,
    ).pack(fill="x", padx=16, pady=(16, 8))

    entrada_nome = tk.Entry(janela, width=30)
    entrada_nome.pack(padx=16, pady=8)
    entrada_nome.focus()

    tk.Button(
        janela,
        text="Enviar",
        command=mostrar_nome,
        width=20,
        background="blue",
        foreground="yellow",
    ).pack(padx=16, pady=(8, 16))

    janela.bind("<Return>", lambda _evento: mostrar_nome())
    janela.mainloop()


if __name__ == "__main__":
    main()
