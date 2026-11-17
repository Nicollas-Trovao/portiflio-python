import csv
import os
import tempfile
import unittest

from trabalho_python.database import Database
from trabalho_python.services import (ATENDIDA, EM_ATENDIMENTO, PENDENTE,
                                SolicitacaoService, TransicaoInvalidaError,
                                ValidacaoError)


class TesteTrabalhoPython(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp.name, "teste.db")
        self.service = SolicitacaoService(Database(self.db_path))

    def tearDown(self):
        self.tmp.cleanup()

    def test_cadastro_inicia_pendente(self):
        s = self.service.criar("TI", "Mouse USB", "5", "Alta")
        self.assertEqual(s.status, PENDENTE)
        self.assertEqual((s.quantidade, s.prioridade), (5, "Alta"))
        self.assertTrue(s.data_hora)

    def test_quantidade_invalida_recusada(self):
        for qtd in ("0", "-3", "2.5", "abc", "", "  "):
            with self.assertRaises(ValidacaoError, msg=qtd):
                self.service.criar("Administrativo", "Papel A4", qtd, "Normal")
        self.assertEqual(self.service.listar(), [])

    def test_campos_vazios_recusados(self):
        with self.assertRaises(ValidacaoError):
            self.service.criar("", "Mouse", "1", "Normal")
        with self.assertRaises(ValidacaoError):
            self.service.criar("TI", "   ", "1", "Normal")

    def test_fluxo_e_bloqueio_de_transicoes(self):
        s = self.service.criar("TI", "Mouse USB", "5", "Alta")
        with self.assertRaises(TransicaoInvalidaError):
            self.service.concluir(s.id)
        self.assertEqual(self.service.iniciar_atendimento(s.id).status, EM_ATENDIMENTO)
        with self.assertRaises(TransicaoInvalidaError):
            self.service.iniciar_atendimento(s.id)
        self.assertEqual(self.service.concluir(s.id).status, ATENDIDA)
        with self.assertRaises(TransicaoInvalidaError):
            self.service.concluir(s.id)

    def test_persistencia_apos_reabrir(self):
        s = self.service.criar("TI", "Mouse USB", "5", "Alta")
        novo = SolicitacaoService(Database(self.db_path))
        self.assertEqual(novo.obter(s.id).material, "Mouse USB")

    def test_busca_e_filtro(self):
        a = self.service.criar("TI", "Mouse USB", "5", "Alta")
        self.service.criar("Administrativo", "Papel A4", "10", "Normal")
        self.service.iniciar_atendimento(a.id)
        self.service.concluir(a.id)
        self.assertEqual(len(self.service.listar("Mouse")), 1)
        self.assertEqual(len(self.service.listar("TI")), 2)
        self.assertEqual(len(self.service.listar("TI", ATENDIDA)), 1)
        self.assertEqual(len(self.service.listar("100%")), 0)
        self.assertEqual(len(self.service.listar("", ATENDIDA)), 1)
        self.assertEqual(len(self.service.listar("Papel", ATENDIDA)), 0)
        self.assertEqual(len(self.service.listar()), 2)

    def test_sql_injection_nao_funciona(self):
        self.service.criar("TI", "Mouse", "1", "Normal")
        self.assertEqual(self.service.listar("' OR '1'='1"), [])

    def test_exportar_csv(self):
        self.service.criar("TI", "Mouse USB", "5", "Alta")
        caminho = os.path.join(self.tmp.name, "hist.csv")
        self.assertEqual(self.service.exportar_csv(caminho), 1)
        with open(caminho, encoding="utf-8-sig", newline="") as f:
            linhas = list(csv.reader(f, delimiter=";"))
        self.assertEqual(linhas[0], ["ID", "Setor", "Material", "Quantidade",
                                     "Prioridade", "Status", "Data/Hora"])
        self.assertEqual(linhas[1][1:6],
                         ["TI", "Mouse USB", "5", "Alta", "Pendente"])


if __name__ == "__main__":
    unittest.main()
