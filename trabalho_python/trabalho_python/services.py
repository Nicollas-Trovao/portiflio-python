import csv
from dataclasses import dataclass
from datetime import datetime
from typing import List

from .database import Database

PENDENTE = "Pendente"
EM_ATENDIMENTO = "Em atendimento"
ATENDIDA = "Atendida"

STATUS_LISTA = [PENDENTE, EM_ATENDIMENTO, ATENDIDA]
PRIORIDADES = ["Normal", "Alta"]

TRANSICOES = {
    PENDENTE: EM_ATENDIMENTO,
    EM_ATENDIMENTO: ATENDIDA,
}


class TrabalhoPythonError(Exception):
    pass


class ValidacaoError(TrabalhoPythonError):
    pass


class TransicaoInvalidaError(TrabalhoPythonError):
    pass


@dataclass
class Solicitacao:
    id: int
    setor: str
    material: str
    quantidade: int
    prioridade: str
    status: str
    data_hora: str

    @property
    def data_hora_br(self) -> str:
        dt = datetime.strptime(self.data_hora, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%d/%m/%Y %H:%M:%S")

    @classmethod
    def de_linha(cls, linha) -> "Solicitacao":
        return cls(**{k: linha[k] for k in linha.keys()})


class SolicitacaoService:
    def __init__(self, db: Database):
        self.db = db

    @staticmethod
    def validar(setor: str, material: str, quantidade: str, prioridade: str):
        setor = (setor or "").strip()
        material = (material or "").strip()
        quantidade = (str(quantidade) if quantidade is not None else "").strip()
        prioridade = (prioridade or "").strip()

        if not setor:
            raise ValidacaoError("O campo Setor é obrigatório.")
        if not material:
            raise ValidacaoError("O campo Material é obrigatório.")
        if not quantidade:
            raise ValidacaoError("O campo Quantidade é obrigatório.")
        if not (quantidade.isascii() and quantidade.isdigit()) or int(quantidade) <= 0:
            raise ValidacaoError("A quantidade deve ser um número inteiro positivo.")
        if prioridade not in PRIORIDADES:
            raise ValidacaoError("Selecione a prioridade: Normal ou Alta.")
        return setor, material, int(quantidade), prioridade

    def criar(self, setor: str, material: str, quantidade: str,
              prioridade: str) -> Solicitacao:
        setor, material, qtd, prioridade = self.validar(
            setor, material, quantidade, prioridade)
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        novo_id = self.db.inserir(setor, material, qtd, prioridade, PENDENTE, agora)
        return self.obter(novo_id)

    def obter(self, id_: int) -> Solicitacao:
        linha = self.db.buscar_por_id(id_)
        if linha is None:
            raise TrabalhoPythonError(f"Solicitação #{id_} não encontrada.")
        return Solicitacao.de_linha(linha)

    def _transicionar(self, id_: int, de: str, para: str) -> Solicitacao:
        sol = self.obter(id_)
        if sol.status != de:
            proximo = TRANSICOES.get(sol.status)
            if proximo is None:
                msg = (f"A solicitação #{id_} já está '{sol.status}' "
                       "e não pode ser alterada.")
            else:
                msg = (f"Transição inválida: a solicitação #{id_} está "
                       f"'{sol.status}' e só pode ir para '{proximo}'.")
            raise TransicaoInvalidaError(msg)
        self.db.atualizar_status(id_, para)
        return self.obter(id_)

    def iniciar_atendimento(self, id_: int) -> Solicitacao:
        return self._transicionar(id_, PENDENTE, EM_ATENDIMENTO)

    def concluir(self, id_: int) -> Solicitacao:
        return self._transicionar(id_, EM_ATENDIMENTO, ATENDIDA)

    def listar(self, texto: str = "", status: str = "") -> List[Solicitacao]:
        status = status if status in STATUS_LISTA else ""
        linhas = self.db.listar((texto or "").strip(), status)
        return [Solicitacao.de_linha(l) for l in linhas]

    @staticmethod
    def _seguro(valor: str) -> str:
        if valor and valor[0] in "=+-@":
            return "'" + valor
        return valor

    def exportar_csv(self, caminho: str) -> int:
        solicitacoes = list(reversed(self.listar()))
        with open(caminho, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["ID", "Setor", "Material", "Quantidade",
                        "Prioridade", "Status", "Data/Hora"])
            for s in solicitacoes:
                w.writerow([s.id, self._seguro(s.setor), self._seguro(s.material),
                            s.quantidade, s.prioridade, s.status, s.data_hora_br])
        return len(solicitacoes)
