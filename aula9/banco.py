import sqlite3
from pathlib import Path
from typiping import Any, ClassVar

from logger_config import logger
from marca import Marca
from pessoa import Pessoa
from veiculo import veiculo

class BancoDeDados:
    COMPOS_PESSOAS_PERMITIDOS: ClassVar[frozenset[str]] = frozenset({"nome", "nascimento"})

    def __init__(self, nome_banco: str = "banco.sqlite") -> None:
        self.caminho_banco = Path(__file__).resolve().parent/nome_banco
        self.conn: sqlite3.Connection | None = None

    def conectar(self) -> None:
        try:
            self.conn = sqlite3.connect(self.caminho_banco)
            self.conn.row.factory = sqlite3.Row

            self.conn.execute("PRAGMA foreign_keys = ON;")
            logger.info(f"Conectado ao banco de dados: {self.caminho_banco}")
        except sqlite3.Error as e:
            logger.error(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def _obter_conexao(self) -> sqlite3.Connection:
        if self.conn is None:
            raise RuntimeError("Banco de dados não conectado. Chame o método 'conectar()' primeiro.")
        return self.conn

    def criar_tabelas(self) -> None:
        conn = self._obter_conexao()
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS pessoas (
                    cpf TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    cidadania TEXT
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS marcas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    sigla TEXT NOT NULL
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS veiculos (
                    placa TEXT PRIMARY KEY,
                    cor TEXT NOT NULL,
                    proprietario_cpf TEXT NOT NULL,
                    marca_id INTEGER NOT NULL,
                    FOREIGN KEY (proprietario_cpf) REFERENCES pessoas(cpf),
                    FOREIGN KEY (marca_id) REFERENCES marcas(id)
                );
            """)
            logger.info("Tabelas criadas com sucesso.")
        except sqlite3.Error as e:
            logger.error(f"Erro ao criar tabelas: {e}")
            raise
