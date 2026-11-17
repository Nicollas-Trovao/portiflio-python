import sqlite3
from pathlib import Path
from tkinter import messagebox, ttk

class Database:
    def __init__(self, caminho: str | Path = "usuario.db") -> None:
        self.conn = sqlite3.connect(caminho)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        self.conn.commit()

def inserir(self, nome: str, email: str) -> None:
        with self.conn:
             self.conn.execute("INSERT INTO usuario (nome, email) VALUES (?, ?)", (nome, email))

def autualizar(self, id: int, nome: str, email: str) -> None:
        with self.conn:
            self.conn.execute("UPDATE usuario SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
def excluir(self, id: int) -> None:
        with self.conn:
            self.conn.execute("DELETE FROM usuario WHERE id = ?", (id,))

def fechar(self) -> None:
        self.conn.close()

class CadastroApp(ttk.Frame):
    def __init__(self, master: tk.Tk, db: Database) -> None:
        super().__init__(master, padding = 20)
        self.db = db
        self.pack(fill = "both", expand = True)
        master.title("Cadastro de Usuários")
        master.geometry("850x490")

        botoes = ttk.Frame(self)
        botoes.pack(fill = "x", pady = (0, 12))
        ttk.Button(botoes, text = "Novo", command = self.novo).pack(side = "left")
        ttk.Button(botoes, text = "Editar", command = self.salvar).pack(side = "left", padx = 6)
        ttk.Button(botoes, text = "Excluir", command = self.excluir).pack(side = "left")
    
    self.tree = ttk.Treeview(area, columns = ("id", "nome", "email"), show = "headings", selectmode = "browse")
    for coluna, titulo, largura in ("id", "ID", 60), ("nome", "Nome", 240), ("email", "Email", 390):
        self.tree.heading(coluna, text = titulo)
        self.tree.column(coluna, width = largura, anchor = "w")
    self.tree.pack(side = "left", fill = "both", expand = True)
    barra = ttk.Scrollbar(area, orient = "vertical", command = self.tree.yview)
    barra.pack(side = "right", fill = "y")
    self.tree.configure(yscrollcommand = barra.set)

    def atualizar_tabela(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)
        for id, nome, email in self.db.conn.execute("SELECT id, nome, email FROM usuario"):
            self.tree.insert("", "end", values = (id, nome, email))

    def salvar(self) -> None:
        nome = self.nome.get().strip()
        email = self.email.get().strip()
        if not nome or not email:
             messagebox.showwarning("Aviso", "Nome e Email são obrigatórios.")