import tkinter as tk

from trabalho_python.database import Database
from trabalho_python.services import SolicitacaoService
from trabalho_python.ui import App


def main() -> None:
    db = Database("solicitacoes.db")
    service = SolicitacaoService(db) #conectou amen!!!
    root = tk.Tk()
    App(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
