# Trabalho Python — Central dos Materiais

Sistema desktop para organizar pedidos internos de materiais (cabos, periféricos,
papel, itens de escritório), acompanhar a equipe e consultar o histórico.
Trabalho individual de **Desenvolvimento Rápido de Aplicações em Python (2026.2)**.

**Autor:** _(seu nome e matrícula aqui)_

## Requisitos

- **Python 3.9 ou superior** (desenvolvido com Python 3.12)
- Tkinter (já vem com o Python no Windows/macOS; no Linux Debian/Ubuntu:
  `sudo apt install python3-tk`)
- **Nenhuma dependência externa** — apenas biblioteca padrão (`tkinter`, `sqlite3`,
  `csv`, `datetime`, `unittest`). Por isso o `requirements.txt` não lista pacotes.

## Como executar

```bash
git clone <link-do-repositorio>
cd trabalho_python
python main.py
```

O arquivo `solicitacoes.db` é criado automaticamente na primeira execução, na pasta
em que o comando é executado.

## Funcionalidades

- **Cadastro** de Setor, Item, Quantidade e Urgência (Normal/Alta). O número e a
  data/hora são gerados automaticamente e o status inicial é **Pendente**.
- **Validações:** campos vazios são bloqueados; a quantidade deve ser um inteiro
  positivo (recusa `0`, negativos, decimais e texto).
- **Fluxo de atendimento:** `Pendente → Em atendimento → Atendida`, com um botão para
  cada ação. Transições inválidas (pular etapa ou repetir) são bloqueadas com aviso.
- **Persistência** em SQLite, sempre com consultas parametrizadas (`?`).
- **Pesquisa** por Setor ou Material (por trecho, sem diferenciar maiúsculas de
  minúsculas), **filtro por Status** e botão **Limpar filtros**. A tabela é
  atualizada após cada operação.
- **Exportação CSV** do histórico completo com cabeçalho
  (`ID;Setor;Material;Quantidade;Prioridade;Status;Data/Hora`). Usa `;` como
  separador e UTF-8 com BOM para abrir corretamente no Excel em português.

## Estrutura do projeto

```
trabalho_python/
├── main.py                 # ponto de entrada
├── requirements.txt
├── README.md
├── trabalho_python/
│   ├── database.py         # acesso ao SQLite (SQL parametrizado)
│   ├── services.py         # regras de negócio: validação, fluxo de status, CSV
│   └── ui.py               # interface Tkinter/ttk (sem SQL e sem regras)
└── tests/
    └── test_services.py    # testes automatizados das regras
```

Separação de responsabilidades: a **interface** só coleta dados e exibe mensagens; as
**regras de negócio** (`SolicitacaoService`) decidem o que é válido; o **banco**
(`Database`) apenas lê e grava.

## Testes

### Testes manuais (pela interface)

1. Cadastre **TI / Mouse USB / 5 / Alta** → a linha aparece com status **Pendente**.
2. Tente cadastrar **Administrativo / Papel A4 / 0 / Normal** → a operação é recusada
   com mensagem de erro e nada é gravado.
3. Selecione o registro e clique em **Iniciar atendimento** (→ Em atendimento) e depois
   em **Concluir** (→ Atendida). Tente **Concluir** de novo → é bloqueado.
4. Feche o programa e abra de novo (`python main.py`) → o registro continua na tabela.
5. Pesquise **Mouse** e depois **TI**, filtre por **Atendida** e use **Exportar CSV**;
   abra o arquivo gerado e confira o cabeçalho e os dados.

### Testes automatizados

```bash
python -m unittest -v
```

Cobrem: cadastro com status Pendente, recusa de quantidade inválida e campos vazios,
fluxo e bloqueio de transições, persistência após reabrir o banco, busca e filtro,
tentativa de SQL injection e conteúdo do CSV.

## Uso de ferramentas de IA

_(Preencha com sinceridade antes de entregar. Exemplo:)_ Utilizei o Claude (Anthropic)
para gerar a primeira versão do código a partir do enunciado. Depois li e testei cada
módulo, e consigo explicar as decisões principais: separação em três camadas, uso de
`?` nas consultas, tabela de transições de status e exportação CSV com `;` e BOM.
