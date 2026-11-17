import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox, ttk

from .services import (ATENDIDA, EM_ATENDIMENTO, PENDENTE, PRIORIDADES,
                       STATUS_LISTA, SolicitacaoService, TrabalhoPythonError)

TODOS = "Todos"
STATUS_DIVERTIDOS = {
    PENDENTE: "Na fila",
    EM_ATENDIMENTO: "Em ação",
    ATENDIDA: "Tudo certo",
}
STATUS_TECNICOS = {nome: status for status, nome in STATUS_DIVERTIDOS.items()}


class App(ttk.Frame): #janelin feita
    def __init__(self, master: tk.Tk, service: SolicitacaoService):
        super().__init__(master, padding=12)
        self.service = service
        self.master.title("Trabalho Python — Central dos Materiais")
        self.master.minsize(900, 560)
        self.pack(fill="both", expand=True)

        self.var_setor = tk.StringVar()
        self.var_material = tk.StringVar()
        self.var_quantidade = tk.StringVar()
        self.var_prioridade = tk.StringVar(value=PRIORIDADES[0])
        self.var_busca = tk.StringVar()
        self.var_filtro = tk.StringVar(value=TODOS)
        self.var_info = tk.StringVar()

        self._montar_formulario()
        self._montar_busca()
        self._montar_tabela()
        self._montar_acoes()
        ttk.Label(self, textvariable=self.var_info, anchor="w").pack(
            fill="x", pady=(8, 0))
        self.atualizar_tabela()

    def _montar_formulario(self):
        box = ttk.LabelFrame(self, text="Criar um pedido", padding=10)
        box.pack(fill="x")

        ttk.Label(box, text="Equipe:").grid(row=0, column=0, sticky="w")
        self.ent_setor = ttk.Entry(box, textvariable=self.var_setor, width=22)
        self.ent_setor.bind("<Return>", lambda _e: self.cadastrar())
        self.ent_setor.grid(row=0, column=1, padx=(4, 12))

        ttk.Label(box, text="O que precisa?:").grid(row=0, column=2, sticky="w")
        ent_mat = ttk.Entry(box, textvariable=self.var_material, width=26)
        ent_mat.grid(row=0, column=3, padx=(4, 12))
        ent_mat.bind("<Return>", lambda _e: self.cadastrar())

        ttk.Label(box, text="Quantas unidades?:").grid(row=0, column=4, sticky="w")
        ent_qtd = ttk.Entry(box, textvariable=self.var_quantidade, width=8)
        ent_qtd.grid(row=0, column=5, padx=(4, 12))
        ent_qtd.bind("<Return>", lambda _e: self.cadastrar())

        ttk.Label(box, text="Prioridade:").grid(row=0, column=6, sticky="w")
        ttk.Combobox(box, textvariable=self.var_prioridade, values=PRIORIDADES,
                     state="readonly", width=9).grid(row=0, column=7, padx=(4, 12))

        ttk.Button(box, text="Mandar pro time", command=self.cadastrar).grid(
            row=0, column=8)

    def _montar_busca(self): #Admito q peguei essa parte da internet
        box = ttk.LabelFrame(self, text="Caça-pedidos", padding=10)
        box.pack(fill="x", pady=10)

        ttk.Label(box, text="Equipe ou item:").grid(row=0, column=0)
        ent = ttk.Entry(box, textvariable=self.var_busca, width=30)
        ent.grid(row=0, column=1, padx=(4, 12))
        ent.bind("<Return>", lambda _e: self.atualizar_tabela())

        ttk.Label(box, text="Situação:").grid(row=0, column=2)
        cb = ttk.Combobox(
            box, textvariable=self.var_filtro, state="readonly",
            values=[TODOS] + [STATUS_DIVERTIDOS[s] for s in STATUS_LISTA], width=16)
        cb.grid(row=0, column=3, padx=(4, 12))
        cb.bind("<<ComboboxSelected>>", lambda _e: self.atualizar_tabela())

        ttk.Button(box, text="Encontrar", command=self.atualizar_tabela).grid(
            row=0, column=4, padx=4)
        ttk.Button(box, text="Limpar bagunça", command=self.limpar_filtros).grid(
            row=0, column=5, padx=4)

    def _montar_tabela(self):
        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True)

        colunas = [("id", "Nº", 50), ("setor", "Equipe", 140),
                   ("material", "Item", 200), ("quantidade", "Qtd", 60),
                   ("prioridade", "Urgência", 90), ("status", "Situação", 120),
                   ("data_hora", "Data/Hora", 150)]
        self.tree = ttk.Treeview(frame, columns=[c[0] for c in colunas],
                                 show="headings", selectmode="browse")
        for chave, titulo, largura in colunas:
            ancora = "center" if chave in ("id", "quantidade") else "w"
            self.tree.heading(chave, text=titulo)
            self.tree.column(chave, width=largura, anchor=ancora)

        barra = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=barra.set)
        self.tree.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        self.tree.tag_configure(PENDENTE, background="#fff4d6")
        self.tree.tag_configure(EM_ATENDIMENTO, background="#dcebff")
        self.tree.tag_configure(ATENDIDA, background="#dcf5dc")

    def _montar_acoes(self):
        box = ttk.Frame(self)
        box.pack(fill="x", pady=(10, 0))
        ttk.Button(box, text="▶ Bota pra funcionar",
                   command=self.iniciar_atendimento).pack(side="left")
        ttk.Button(box, text="✔ Missão cumprida",
                   command=self.concluir).pack(side="left", padx=8)
        ttk.Button(box, text="Salvar uma lista…",
                   command=self.exportar_csv).pack(side="right")


    def cadastrar(self):
        try:
            sol = self.service.criar(self.var_setor.get(), self.var_material.get(),
                                     self.var_quantidade.get(),
                                     self.var_prioridade.get())
        except TrabalhoPythonError as e:
            messagebox.showwarning("Dados inválidos", str(e))
            return
        self.var_setor.set("")
        self.var_material.set("")
        self.var_quantidade.set("")
        self.var_prioridade.set(PRIORIDADES[0])
        self.ent_setor.focus_set()
        self.atualizar_tabela()
        situacao = STATUS_DIVERTIDOS.get(sol.status, sol.status)
        self.var_info.set(f"Pedido #{sol.id} entrou na linha como {situacao}.")

    def _id_selecionado(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Selecione uma solicitação",
                                "Clique em uma linha da tabela primeiro.")
            return None
        return int(sel[0])

    def _executar_transicao(self, funcao):
        id_ = self._id_selecionado()
        if id_ is None:
            return
        try:
            sol = funcao(id_)
        except TrabalhoPythonError as e:
            messagebox.showwarning("Ação não permitida", str(e))
            return
        self.atualizar_tabela()
        if self.tree.exists(str(id_)):
            self.tree.selection_set(str(id_))
        situacao = STATUS_DIVERTIDOS.get(sol.status, sol.status)
        self.var_info.set(f"Pedido #{sol.id} ganhou novo status: {situacao}.")

    def iniciar_atendimento(self):
        self._executar_transicao(self.service.iniciar_atendimento)

    def concluir(self):
        self._executar_transicao(self.service.concluir)

    def limpar_filtros(self):
        self.var_busca.set("")
        self.var_filtro.set(TODOS)
        self.atualizar_tabela()

    def atualizar_tabela(self):
        filtro = self.var_filtro.get()
        status = "" if filtro == TODOS else STATUS_TECNICOS.get(filtro, "")
        solicitacoes = self.service.listar(self.var_busca.get(), status)
        self.tree.delete(*self.tree.get_children())
        for s in solicitacoes:
            self.tree.insert("", "end", iid=str(s.id), tags=(s.status,), values=(
                s.id, s.setor, s.material, s.quantidade, s.prioridade,
                STATUS_DIVERTIDOS.get(s.status, s.status), s.data_hora_br))
        self.var_info.set(f"{len(solicitacoes)} solicitação(ões) exibida(s).")

    def exportar_csv(self):
        sugestao = f"historico_trabalho_python_{datetime.now():%Y%m%d_%H%M%S}.csv"
        caminho = filedialog.asksaveasfilename(
            title="Exportar histórico", defaultextension=".csv",
            initialfile=sugestao, filetypes=[("Arquivo CSV", "*.csv")])
        if not caminho:
            return
        try:
            total = self.service.exportar_csv(caminho)
        except OSError as e:
            messagebox.showerror("Erro ao exportar", f"Não foi possível salvar:\n{e}")
            return
        messagebox.showinfo("Exportação concluída",
                            f"{total} registro(s) exportado(s) para:\n{caminho}")
