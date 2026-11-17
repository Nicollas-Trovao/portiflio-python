import sqlite3
from contextlib import closing
from typing import List, Optional

SCHEMA = """
CREATE TABLE IF NOT EXISTS solicitacoes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    setor       TEXT    NOT NULL,
    material    TEXT    NOT NULL,
    quantidade  INTEGER NOT NULL CHECK (quantidade > 0),
    prioridade  TEXT    NOT NULL,
    status      TEXT    NOT NULL,
    data_hora   TEXT    NOT NULL
)
"""
#Eu não aguento mais...

class Database:
    def __init__(self, caminho: str = "solicitacoes.db"):
        self.caminho = caminho
        self._criar_tabelas()

    def _conectar(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.caminho)
        conn.row_factory = sqlite3.Row
        return conn

    def _criar_tabelas(self) -> None:
        with closing(self._conectar()) as conn, conn:
            conn.execute(SCHEMA)

    def inserir(self, setor: str, material: str, quantidade: int,
                prioridade: str, status: str, data_hora: str) -> int:
        with closing(self._conectar()) as conn, conn:
            cur = conn.execute(
                "INSERT INTO solicitacoes "
                "(setor, material, quantidade, prioridade, status, data_hora) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (setor, material, quantidade, prioridade, status, data_hora),
            )
            return cur.lastrowid

    def buscar_por_id(self, id_: int) -> Optional[sqlite3.Row]:
        with closing(self._conectar()) as conn:
            return conn.execute(
                "SELECT * FROM solicitacoes WHERE id = ?", (id_,)
            ).fetchone()

    def listar(self, texto: str = "", status: str = "") -> List[sqlite3.Row]:
        sql = "SELECT * FROM solicitacoes WHERE 1=1"
        params: list = []
        if texto:
            sql += (" AND (setor LIKE ? ESCAPE '\\' "
                    "OR material LIKE ? ESCAPE '\\')")
            escapado = (texto.replace("\\", "\\\\")
                        .replace("%", "\\%").replace("_", "\\_"))
            padrao = f"%{escapado}%"
            params += [padrao, padrao]
        if status:
            sql += " AND status = ?"
            params.append(status)
        sql += " ORDER BY id DESC"
        with closing(self._conectar()) as conn:
            return conn.execute(sql, params).fetchall()

    def atualizar_status(self, id_: int, novo_status: str) -> None:
        with closing(self._conectar()) as conn, conn:
            conn.execute(
                "UPDATE solicitacoes SET status = ? WHERE id = ?",
                (novo_status, id_),
            )
